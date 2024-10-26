from os import makedirs
from shutil import rmtree
from yaml import safe_load


def create_dir(path):
    makedirs(path, exist_ok=True)


def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()


def write_to_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)


def remove_dir_with_content(dirpath):
    rmtree(dirpath)


def load_yaml(filepath):
    with open(filepath, "r") as f:
        return safe_load(f.read())
