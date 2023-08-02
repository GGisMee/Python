import requests
from pathlib import Path
import importlib
from sys import path

# https://raw.githubusercontent.com/GGisMee/Python/main/libraries/current_directory.py
def import_from_github(https, file_name: str = "chosen from end of link", directory=path[0], load_lib = False):
    """This function is used to import a file to a chosen directory using a github raw link
    
    args:
        https: A  github raw website string.
        file_name: The name chosen for the file imported.
        directory: Chosen directory to place the file in
        load_lib: if the library should be returned

    Returns:
        bool: True or False, Success or Fail
        if load_lib: Library
        """
    file_name = "/".join(map(str,(https.split("/")[-1:]))) if file_name == "chosen from end of link" else file_name
    
    file_path = f"{directory}/{file_name}"
    if Path(file_path).is_file():
        print(f"{file_path} already exists")
    else:
        print(f"{file_path} doesn't exist, download")
        request = requests.get(https)
        with open(file_path, "wb") as f:
            f.write(request.content)
    file_name = file_name.split(".")[0]
    if load_lib:
        module_spec = importlib.util.spec_from_file_location(file_name, file_path)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module
    return True

def import_from_path(file_name, directory):
    """imports a file from path
    
    tip: use r'directory', to not have to worry about SyntaxError
    
    args:
        file_name: The name of the file to import.
        directory: the directory which the file comes from
    
    returns:
        bool: False if fail, library is true
    """
    file_path = f"{directory}/{file_name}"
    if not Path(file_path).is_file():
        print("file doesn't exist")
        return False
    module_spec = importlib.util.spec_from_file_location(file_name, file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    return module
        
