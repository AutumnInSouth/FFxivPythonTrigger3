import hashlib
import os


def dir_hash(directory_path):
    hashs = hashlib.sha256()
    if not os.path.exists(directory_path):
        return None
    for root, dirs, files in os.walk(directory_path):
        for names in files:
            filepath = os.path.join(root, names)
            with open(filepath, 'rb') as f1:
                while True:
                    buf = f1.read(4096)
                    if not buf: break
                    hashs.update(hashlib.sha256(buf).digest())
    return hashs.hexdigest()


def file_hash(file_path):
    if not os.path.exists(file_path):
        return None
    hashs = hashlib.sha256()
    with open(file_path, 'rb') as f1:
        while True:
            buf = f1.read(4096)
            if not buf: break
            hashs.update(hashlib.sha256(buf).digest())
    return hashs.hexdigest()


def get_hash(path):
    if os.path.isdir(path):
        return dir_hash(path)
    else:
        return file_hash(path)
