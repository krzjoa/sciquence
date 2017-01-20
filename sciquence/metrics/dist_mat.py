# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Functions for computing distance matrices
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np



def cosine_dm(A, B):
    '''

    Compute cosine distance matrix between two
    matrices A and B. Heights of both matrices must match.

    Parameters
    ----------
    A: ndarray (n_samples, n_features)
        Matrix A
    B: ndarray (n_samples, n_features)
        Matrix B

    Returns
    -------
    dist_mat: ndarray(n_samples_A, n_samples_b)
        A distance matrix

    '''
    A = A / np.sqrt(np.sum(A ** 2, axis=0))[None, :]
    B = B / np.sqrt(np.sum(B ** 2, axis=0))[None, :]
    return B.T.dot(A)



