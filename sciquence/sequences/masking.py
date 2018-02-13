

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


def make_masked_input(list_of_seq):
    '''

    Make mask for sequences and coherent seqences block

    Parameters
    ----------
    list_of_seq: list of Iterable
        List of numpy array

    Returns
    -------
    mask: numpy.ndarray
        Mask
    '''

    lens = [len(seq) for seq in list_of_seq]
    N, M = len(lens), max(lens)

    mask = np.zeros((N, M))
    input = np.zeros((N, M))

    for i, l in enumerate(lens):
        mask[i, :l] = 1.
        input[i, :l] = list_of_seq[i]
    return input, mask


def make_masked_rnn_input(*ls):
    '''

    RNN input

    Parameters
    ----------
    ls: list of Iterable
        List of numpy array

    Returns
    -------
    mask: numpy.ndarray
         Mask
    '''

    list_of_seq = ls[0]

    lens = [seq.shape[1] for seq in list_of_seq]
    N, M, L = len(lens), max(lens), list_of_seq[0].shape[-1]

    mask = np.zeros((N, M, L))
    input = [np.zeros((N, M, L)) for i in xrange(len(ls))]

    # import pdb
    # pdb.set_trace()

    for i, l in enumerate(lens):
        mask[i, :l, :] = 1.

        for il in xrange(len(ls)):

            # import pdb
            # pdb.set_trace()

            input[il][i, :l, :] = ls[il][i]


    input += [mask]

    return input

