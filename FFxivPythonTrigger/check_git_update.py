from copy import deepcopy
from datetime import timezone, datetime
from os import getcwd
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from requests import get

from .storage import ModuleStorage, BASE_PATH

api_domain = "https://api.github.com"
base_domain = "https://github.com"
_update_res_path = Path(getcwd()) / '.update_res'
_update_res_path.mkdir(exist_ok=True)
_storage = ModuleStorage(BASE_PATH / "Update")
headers = {'User-Agent': 'FFxivPythonTrigger', }


class CheckUpdateException(Exception):
    pass


def compare_file(src: Path, dst: Path):
    try:
        return compare_text_file(src, dst)
    except UnicodeDecodeError:
        with src.open('rb') as f1, dst.open('rb') as f2:
            return f1.read() == f2.read()


def compare_text_file(src: Path, dst: Path):
    with src.open('r', encoding='utf8') as f1, dst.open('r', encoding='utf8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        line_ptr1 = line_ptr2 = 0
        while True:
            if line_ptr1 >= len(lines1):
                while line_ptr2 < len(lines2):
                    if lines2[line_ptr2].strip(): return False
                    line_ptr2 += 1
                return True
            if line_ptr2 >= len(lines2):
                while line_ptr1 < len(lines1):
                    if lines1[line_ptr1].strip(): return False
                    line_ptr1 += 1
                return True

            if not lines1[line_ptr1].strip():  # skip empty lines
                line_ptr1 += 1
                continue
            if not lines2[line_ptr2].strip():  # skip empty lines
                line_ptr2 += 1
                continue
            if lines1[line_ptr1].strip() != lines2[line_ptr2].strip():
                return False
            line_ptr1 += 1
            line_ptr2 += 1


def date_to_timestamp(date: str):
    return int(datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc).timestamp())


default_repo_data = {
    'client_last_update': '',
    'remote_last_update': {
        'etag': '',
        'date': '',
    },
    'new_commits': {
        'etag': '',
        'commits': {},
        'res': [],
    },
}


def get_repo_data(repo: str):
    return _storage.data.setdefault(repo, deepcopy(default_repo_data))


def get_last_update_date(repo: str):
    repo_data = get_repo_data(repo)['remote_last_update']
    headers_ = headers.copy()
    headers_["If-None-Match"] = repo_data['etag']
    try:
        res = get(f"{api_domain}/repos/{repo}/commits", {'page': '1', 'per_page': '1'}, headers=headers_)
    except Exception as e:
        raise CheckUpdateException(f"Error while checking update: {e}")
    if res.status_code != 304:
        data = res.json()
        if res.status_code != 200:
            raise CheckUpdateException(data["message"])
        repo_data['etag'] = res.headers['ETag']
        repo_data['date'] = data[0]["commit"]["author"]["date"]
        _storage.save()
    return repo_data['date']


def get_update_commit(repo: str):
    repo_data = get_repo_data(repo)
    new_commits_data = repo_data['new_commits']
    headers_ = headers.copy()
    headers_["If-None-Match"] = new_commits_data['etag']
    param = {'page': '1', 'per_page': '100'}
    if repo_data['client_last_update']:
        param['since'] = repo_data['client_last_update']
    try:
        res = get(f"{api_domain}/repos/{repo}/commits", param, headers=headers_)
    except Exception as e:
        raise CheckUpdateException(f"Error while checking new commits: {e}")
    if res.status_code != 304:
        data = res.json()
        if res.status_code != 200:
            raise CheckUpdateException(data["message"])
        new_commits_data['etag'] = res.headers['ETag']
        res = []
        for commit in data:
            if commit['sha'] not in new_commits_data['commits']:
                commit_data = {
                    'sha': commit['sha'],
                    'message': commit['commit']['message'],
                    'date': commit['commit']['author']['date'],
                    'modified_files': [],
                }
                try:
                    _res = get(f"{api_domain}/repos/{repo}/commits/{commit['sha']}", headers=headers)
                except Exception as e:
                    raise CheckUpdateException(f"Error while checking new commits: {e}")
                _data = _res.json()
                if _res.status_code != 200:
                    raise CheckUpdateException(_data["message"])
                for file in _data['files']:
                    commit_data['modified_files'].append(file['filename'])
                new_commits_data['commits'][commit['sha']] = commit_data
                res.append(commit['sha'])
        new_commits_data['res'] = res
        _storage.save()
    return [new_commits_data['commits'][sha] for sha in new_commits_data['res']]


def process_update(repo: str, base_path: Path | str, force_update: bool = False):
    if isinstance(base_path, str): base_path = Path(base_path)
    repo_update_path = _update_res_path / repo.replace('/', '_')
    repo_update_path.mkdir(exist_ok=True)
    latest = get_last_update_date(repo)
    repo_data = get_repo_data(repo)
    is_init = not repo_data['client_last_update'] or force_update
    if not force_update and latest == repo_data['client_last_update']:
        raise CheckUpdateException("No update")

    if not is_init:
        update_files = set()
        for c in get_update_commit(repo):
            for file in c['modified_files']:
                update_files.add(file)
    else:
        update_files = None

    update_zip = repo_update_path / f"{date_to_timestamp(latest)}.zip"

    if not update_zip.exists():
        # download master zip file from github
        try:
            # https://github.com/nyaoouo/FFxivPythonTrigger3/archive/master.zip
            res = get(f"{base_domain}/{repo}/archive/master.zip", headers=headers)
        except Exception as e:
            raise CheckUpdateException(f"Error while downloading update: {e}")
        if res.status_code != 200:
            raise CheckUpdateException(res.json()["message"])
        with open(update_zip, 'wb') as f:
            f.write(res.content)

    # unzip update file to a temp directory
    backup_files = []
    with TemporaryDirectory() as tmp_dir, ZipFile(update_zip) as zip_file:
        zip_file.extractall(tmp_dir)
        tmp_dir = Path(tmp_dir) / zip_file.namelist()[0]
        # iter all files in the temp directory ,
        # if same file exists in the base directory and with different content,
        # copy a backup of the old file with adding prefix backup
        # then copy the new file to the base directory

        if is_init:
            files = tmp_dir.glob('**/*')
        else:
            files = (file for file in tmp_dir.glob('**/*') if file.relative_to(tmp_dir) not in update_files)

        for file in files:
            if file.is_file():
                relative_path = file.relative_to(tmp_dir)
                file_path = base_path / relative_path
                # print(f"{file} => {file_path}")
                if file_path.exists():
                    if not compare_file(file, file_path):
                        backup_path = file_path.parent / f"{file_path.stem}.backup{file_path.suffix}"
                        backup_files.append((relative_path, backup_path))
                        # print(f"backup {file_path} => {backup_path}")
                        if backup_path.exists():
                            backup_path.unlink()
                        file_path.rename(backup_path)
                    else:
                        continue
                else:
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                file.rename(file_path)
    repo_data['client_last_update'] = latest
    repo_data['new_commits'] = deepcopy(default_repo_data['new_commits'])
    _storage.save()
    return backup_files
