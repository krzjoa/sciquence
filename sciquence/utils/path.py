import os

def listdir_with_extension(path, extension):
    '''
    
    List all the files in direction with the given extension only
    
    Parameters
    ----------
    path: str
        Directory path
    extension: str
        Extension

    Returns
    -------
    file_list: list of str
        List of files in the given directory
    
    '''
    ls = os.listdir(path)
    return [p for p in ls if p.endswith(extension)]
