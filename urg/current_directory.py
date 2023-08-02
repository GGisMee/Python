from sys import path

def path_dir_with_level(level:int=0) -> str:
    """This is a function which returns the current directory from a level of deepness
    Denna funktionen ger nuvarande foldern eller tidigare foldrar med ett visst djup
    
    args: 
        level (int): the level of depth from current directory
        
    returns:
        bool: False if fail
        str: path with depth"""
    if not isinstance(level, int):
        print("Not type int")
        return False
    return "/".join(map(str,(path[0].split("\\")[:-level]))) if level != 0 else path[0]