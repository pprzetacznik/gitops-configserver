from os import makedirs


def create_dir(path):
    makedirs(path, exist_ok=True)


def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()
