

def load_txt(path):
    '''

    Load text file

    Parameters
    ----------
    path: str
        Path to text file

    Returns
    -------
    f: file
        Text file

    '''
    with open(path, mode='r') as f:
        return f


