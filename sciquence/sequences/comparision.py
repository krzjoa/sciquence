# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Comparision
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def lseq_equal(lseqa, lseqb):
    '''

    Compare two lists of ndarrays

    Parameters
    ----------
    lseqa: list of ndarray
        List of sequences
    lseqb: list of ndarray
        List of sequences

    Returns
    -------
    ans: bool
        True if lists equal, otherwise False

    Examples
    --------
    >>> from sciquence import sequences as sq
    >>> import numpy as np
    >>> x = [np.array([1, 2, 3, 4]), np.array([6, 7, 8])]
    >>> y = [np.array([1., 2.8, 3., 4.]), np.array([6.1, 7., 8.5])]
    >>> z = [np.array([1, 2, 3, 4]), np.array([6, 7, 8])]
    >>> print sq.lseq_equal(x, y)
    False
    >>> print sq.lseq_equal(x, z)
    True

    '''
    ans = [np.array_equal(a, b) for a, b in zip(lseqa, lseqb)]
    return np.logical_and.reduce(ans)


def shapes_equal(*arrays):
    # TODO: unit tests
    '''

    Check if all the arrays have the same shape.

    Parameters
    ----------
    arrays: ndarrays
        Numpy arrays

    Returns
    -------
    are_equal: bool
        True if all the arrays have the same shape, otherwise False

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.random.rand(1, 2)
    >>> y = np.random.rand(1, 2)
    >>> z = np.random.rand(1, 2, 3)
    >>> sq.shapes_equal(x, y)
    True
    >>> sq.shapes_equal(x, y, z)
    False

    '''
    shapes = [arr.shape for arr in arrays]
    return reduce(cmp, shapes)

def size_equal(*arrays, **kwargs):
    # TODO: unit tests
    '''

    Check if all the arrays have the same length along the particular axis.

    Parameters
    ----------
    arrays: ndarrays
        Numpy arrays
    kwargs:
        * axis: int
            Axis index, default: 0

    Returns
    -------
    are_equal: bool
        True if all the arrays have the same shape, otherwise False

    Examples
    --------
    >>> import sciquence.sequences as sq
    >>> import numpy as np
    >>> x = np.random.rand(1, 2)
    >>> y = np.random.rand(1, 2)
    >>> z = np.random.rand(1, 2, 3)
    >>> v = np.random.rand(2, 2, 3)
    >>> sq.shapes_equal(x, y)
    True
    >>> sq.shapes_equal(x, y, z)
    True
    >>> sq.shapes_equal(x, y, z, v)
    True

    '''

    axis = 0

    if 'axis' in kwargs:
        axis = kwargs['axis']

    sizes = [arr.shape[axis] for arr in arrays]
    print sizes
    return reduce(cmp, sizes)

if __name__ == '__main__':
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    #print chunk(x, 3)

    # print shapes_equal(x, x, z)


    #print (1, 2) == (1, 3)