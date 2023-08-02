from sys import path

def path_dir_with_level(level:int=0) -> str:
    """This is a function which returns the current directory from a level of deepness
    Denna funktionen ger nuvarande foldern eller tidigare foldrar med ett visst djup"""
    return "/".join(map(str,(path[0].split("\\")[:-level]))) if level != 0 else path[0]