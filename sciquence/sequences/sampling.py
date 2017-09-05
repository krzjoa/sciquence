# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Sequence sampling
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def random_slice(array, slice_length, axis=0):
    '''
    Choose a random subsequence of given length
    Parameters
    ----------
    array: ndarray
        A sequence
    slice_length: int
        Length of subsequence
    Returns
    -------
    slice: slice
        A subsequence slice
    '''

    if array.shape[0] < slice_length:
        raise Exception("Slice length cannot be greater than input array length")

    max_possible = array.shape[axis] - slice_length
    first = np.random.randint(0, max_possible)
    last = first + slice_length
    return slice(first, last)

def random_chunk(*arrays, **kwargs):

    # Parsing keyword arguments

    pass