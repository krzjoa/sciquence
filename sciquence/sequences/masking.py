

def mask_sequences(list_of_seq):
    '''
    
    Make mask for sequences.
    Very useful especially for recurrent neural netowrks.
    
    Parameters
    ----------
    list_of_seq: list of numpy.ndarray
        List of numpy array

    Returns
    -------
    mask: numpy.ndarray
        Mask
    '''
    
    lens = [len(seq) for seq in list_of_seq]
    N, M = len(lens), max(lens)
    mask = np.zeros((N, M))
    
    for i, l in enumerate(lens):
        mask[i, :l] = 1.
    return mask  
