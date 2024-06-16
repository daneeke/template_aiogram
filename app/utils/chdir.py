import os


def chdir(path: str):
    file_path = os.path.abspath(path)
    dir_path = os.path.dirname(file_path)
    previous_path = os.path.dirname(dir_path)
    os.chdir(previous_path)
