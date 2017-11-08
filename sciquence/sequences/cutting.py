# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Functions for sequence processing
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
from itertools import groupby

############## Getting sequences ##############

def seq(array):
    '''

    Cut input array into sequences consisting of the same elements

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.seq(x)
    [array([1, 1, 1, 1, 1, 1]), array([0, 0, 0, 0, 0, 0]), array([1, 1, 1, 1, 1]), array([0, 0, 0, 0])]

    '''

    return [np.array(list(group)) for elem, group in groupby(array)]


def specseq(array, element):
    '''

    Return sequences consisting of specific tag

    Parameters
    ----------
    array: ndarray
        Numpy array
    element: object
        Element

    Returns
    -------
    seq_list: list of ndarray
        List of sequences consisting of specific tag

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
    >>> print sq.specseq(x, 44)
    [array([44, 44, 44, 44, 44])]

    '''
    return [np.array(list(group)) for elem, group in groupby(array) if elem == element]



def nseq(array):
    '''

    Returns sequences consisting of zeros

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of negative sequences

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.nseq(x)
    [array([0, 0, 0, 0, 0, 0]), array([0, 0, 0, 0])]]

    '''

    return [np.array(list(group)) for elem, group in groupby(array) if not elem]


def pseq(array):
    '''

    Returns sequences consisting of ones

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of positive sequences

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.nseq(x)
    [array([1, 1, 1, 1, 1, 1]), array([1, 1, 1, 1, 1])]
    '''

    return [np.array(list(group)) for elem, group in groupby(array) if elem]


def seqi(array):
    '''

    Get list of sequences and corresponding list of indices

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences
    idx_list: list of ndarray
        List of seqences indices

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
    >>> print sq.seqi(x)
    ([array([0, 1, 2, 3, 4, 5]), array([6, 7, 8, 9, 10, 11]), array([12]),
    array([13, 14, 15, 16, 17]), array([18, 19]), array([20, 21, 22, 23])],

    '''
    # TODO: optimize
    lseq = seq(array)
    indices = []
    last_index = 0
    for s in lseq:
        indices.append(range(last_index, last_index + len(s)))
        last_index += len(s)
    return lseq, indices


def nseqi(array):
    '''

    Get list of negative sequences indices (i.e. consisting of zeroes)

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences
    idx_list: list of ndarray
        List of seqences indices

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.seqi(x)
    [array([ 6,  7,  8,  9, 10, 11]), array([17, 18, 19, 20])]

   '''
    lseq = seq(array)
    indices = []
    last_index = 0
    nlseq = []

    for s in lseq:
        if s[0] == 0:
            indices.append(np.array(range(last_index, last_index + len(s))))
            nlseq.append(s)
        last_index += len(s)
    return indices


def pseqi(array):
    '''

    Get list of positive sequences indices (i.e. consisting of ones)

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences
    idx_list: list of ndarray
        List of seqences indices

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    >>> print sq.seqi(x)
    [array([0, 1, 2, 3, 4, 5]), array([12, 13, 14, 15, 16])]
    '''
    lseq = seq(array)
    indices = []
    last_index = 0
    plseq = []
    for s in lseq:
        if s[0] == 1:
            indices.append(np.array(range(last_index, last_index + len(s))))
            plseq.append(s)
        last_index += len(s)
    return indices


def specseqi(array, elem):
    '''

    Get list of sequences indices, consisting of specific element

    Parameters
    ----------
    array: ndarray
        Numpy array
    elem: object
        A sequence element

    Returns
    -------
    seq_list: list of ndarray
        List of sequences
    idx_list: list of ndarray
        List of seqences indices

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x =  np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
    >>> print sq.seqi(x)
    [array([13, 14, 15, 16, 17])]

    '''
    lseq = seq(array)
    indices = []
    last_index = 0
    plseq = []
    for s in lseq:
        if s[0] == elem:
            indices.append(np.array(range(last_index, last_index + len(s))))
            plseq.append(s)
        last_index += len(s)
    return indices

############### Splitting into chunks ###########

def chunk(array, chunk_size):
    '''

    Split numpy array into chunks of equal length.

    Parameters
    ----------
    array: ndarray
        A numpy array
    chunk_size: int
        Desired length of a single chunk

    Returns
    -------
    chunks: list of ndarray
        Chunks of equal length

    Examples
    --------
    >>> import numpy as np
    >>> import sciquence.sequences as sq
    >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
    >>> sq.chunk(x, 3)
    [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9]), array([10])]

    '''
    chunks = []
    for i in xrange(0, len(array), chunk_size):
        chunks.append(array[i:i+chunk_size])
    return chunks


if __name__ == '__main__':
    x =  np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
    print specseqi(x, 44)

