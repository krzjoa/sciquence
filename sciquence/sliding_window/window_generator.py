# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Classifying data fragments with sliding window
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def wingen(X, window_size, step=1):
    '''

    Generate subsequences from a single sequence.
    Generator usage reduces memory consumption.

    Parameters
    ----------
    X: ndarray (n_samples, n_features)
        Array of size
    window_size: int
        Size of sliding window
    step: int
        Size of sliding window step

    Yields
    -------
    subsequence: ndarray (window_size, n_features)
        Subsequence from X sequence

    Examples
    --------

    >>> from sciquence.sliding_window import wingen
    >>> import numpy as np
    >>> X = np.array([[1, 2, 3,],
    >>>               [11, 12, 13],
    >>>               [21, 22, 23],
    >>>               [31, 32, 33]])
    >>> print wingen(X, 2, 1).next()
    >>> [[ 1  2  3]
    >>>  [11 12 13]]


    '''
    for i in xrange(0, len(X)-window_size+1, step):
        yield X[i:i+window_size]


def multi_wingen(X, window_size, step):
    '''

    Generate subsequences from a single sequence.
    Generator usage reduces memory consumption.

    Parameters
    ----------
    X: ndarray (n_sequences, n_samples, n_features)
       or list of ndarray (n_samples, n_features)
       3-dimensional array or list of sequences
    window_size: int
        Size of sliding window
    step: int
        Size of sliding window step

    Yields
    -------
    subsequence: ndarray (window_size, n_features)
        Subsequence from X sequence

    '''

    for sequence in X:
        for i in xrange(0, len(sequence)-window_size+1, step):
            yield sequence[i:i+step]