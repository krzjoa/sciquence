# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Sequence sampling
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def random_slice(array_len, slice_length):
    '''

    Choose a random slice of given length

    Parameters
    ----------
    array_len: int
        Array length
    slice_length: int
        Length of subsequence
    Returns
    -------
    slice: slice
        A subsequence slice

    Examples
    --------
    >>> import numpy as np
    >>> import sciquence.sequences as sq
    >>> print sq.random_slice(54, 6)
    slice(15, 21, None)

    '''

    if array_len < slice_length:
        raise Exception("Slice length cannot be greater than input array length")

    max_possible = array_len - slice_length
    first = np.random.randint(0, max_possible)
    last = first + slice_length
    return slice(first, last)


def random_fragments(array_len, frag_len, n):
    '''
    
    Get n disjunctive fragments.
    
    Parameters
    ----------
    array_len: int
        Len of array to be sampled from
    frag_len: int or tuple
        Fragment 
    n: int

    Returns
    -------
    fragments: list of list
        Fragment indices

    '''
    
    # TODO: optimize! Case when 

    # Check if possible
    if array_len < n*frag_len:
        raise ValueError("Cannot sample {} disjunctive "
                         "fragments (len: {}) "
                         "from array of length {}".format(n, frag_len, array_len))

    # List of fragments
    fragments = []
    occupied = []

    while len(fragments) < n:
        # Choose random fragment
        max_possible = array_len - frag_len
        first = np.random.randint(0, max_possible)
        last = first + frag_len

        current_fragment = range(first, last)

        if not is_overlapped(occupied, current_fragment):
            fragments.append(current_fragment)
            occupied += current_fragment

    return fragments


def is_overlapped(idx1, idx2):
    '''
    
    Check, if two list of indices overlap.
    
    Parameters
    ----------
    idx1: list of int
        First list of indices
    idx2: list of int
        Second list of indices
    
    Returns
    -------
    is_overlapped: bool
        True if indices overlap, otherwise: False

    Examples
    --------
    >>> import numpy as np
    >>> import sciquence.sequences as sq
    
    '''
    # TODO: check & optimize!'
    s1 = set(idx1)
    s2 = set(idx2)
    return bool(len(s1.intersection(s2)))


def cut_patches(data, center_indices, pad, ignore_short=False):
    '''
    
    Cut patches around selected centers
        
    Parameters
    ----------
    data: numpy.ndarray
        1-d numpy array
    center_indices: list of int
        List of patch centers
    pad: int
        Padding for both side
    ignore_short: bool
        Ignore patches if are too short

    Returns
    -------
    patches: list of numpy.ndarray
        List of patches

    Examples
    --------
    >>> import numpy as np
    >>> import sciquence.sequences as sq
    >>>

    '''

    # TODO: Add fix length

    patches = []
    max_idx = len(data) - 1

    for ci in center_indices:
        start = ci - pad

        if start < 0 and ignore_short:
            continue
        elif start < 0:
            start = 0

        stop = ci + pad + 1

        if stop > max_idx and ignore_short:
            continue
        elif stop < 0:
            stop = max_idx

        patches.append(data[start:stop])
   
    return patches


def random_chunk(*arrays, **kwargs):

    # Parsing keyword arguments

    pass

if __name__ == '__main__':
    print random_slice(44, 6)