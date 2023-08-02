import requests
from pathlib import Path
import importlib
from sys import path
def importFn(https, file_name: str = "undefined_library.py", directory=path[0]):
    """This file is used to import a file to the current directory using a github raw link"""
    file_path = f"{directory}/{file_name}"
    if Path(file_path).is_file():
        print(f"{file_path} already exists")
    else:
        print(f"{file_path} doesn't exist, download")
        request = requests.get(https)
        with open(file_path, "wb") as f:
            f.write(request.content)
    importlib.import_module(file_name.split(".")[0])
