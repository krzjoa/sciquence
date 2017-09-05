# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Functions for sequence processing
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
from comparision import size_equal



def parallel_sort(*arrays, **kwargs):
    # TODO: improve docstring

    '''
    
    Parallel sort. It always uses values from the first array 
    to sort all them.
    
    arrays: lists or/and ndarrays
        Numpy arrays (at least one)
    kwargs:
        * reverse: bool
            If True, reversed sort is performed

    Returns
    -------
    sorted_arrays: ndarrays
        New arrays, parallely sorted accordingly to the first array's elements

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.array([2., 3., 5., 1.45, 6, 4.2])
    >>> y = np.array([0, 1, 0, 0, 0, 1])
    >>> z = np.array([[0, 1, 56, 67, 90, 100],
    >>>               [78, 34, 13, 49, 25, 101]]).T
    >>> print sq.parallel_sort(x, y, z)
    [array([ 1.45,  2.  ,  3.  ,  4.2 ,  5.  ,  6.  ]),
     array([0, 0, 1, 1, 0, 0]),
     array([[ 67,  49],
            [  0,  78],
            [  1,  34],
            [100, 101],
            [ 56,  13],
            [ 90,  25]])]

    '''
    first_array = arrays[0]

    # First array should be one-dimensional
    if first_array.ndim != 1:
        raise Exception("Number of dimensions different than 1!")

    if not size_equal(*arrays):
        raise Exception("Array shapes do not equal!")

    reverse = False

    if 'reverse' in kwargs:
        reverse = kwargs['reverse']

    # Sorting indices
    idx = range(0, len(first_array))
    sorted_values, sorted_idx = zip(*sorted(zip(first_array, idx), reverse=reverse))
    sorted_idx = list(sorted_idx),

    return [arr[sorted_idx] for arr in arrays]

if __name__ == '__main__':

    x = np.array([2., 3., 5., 1.45, 6, 4.2])
    y = np.array([0, 1, 0, 0, 0, 1])
    z = np.array([[0, 1, 56, 67, 90, 100],
                 [78, 34, 13, 49, 25, 101]]).T
    print parallel_sort(x, y, z)
