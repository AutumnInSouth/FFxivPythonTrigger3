from pathlib import Path

from git import Repo, InvalidGitRepositoryError

p = Path(__file__).parent
repo_master = 'git@github.com:nyaoouo/FFxivPythonTrigger3.git'
try:
    repo = Repo(p)
except InvalidGitRepositoryError:
    repo = Repo.clone_from(repo_master, p, branch='master')
