
import numpy as np


# Udemy course
def init_weights(n, m):
    return (np.random.rand(n, m) / np.sqrt(n + m)).astype(np.float32)


def all_parity_pairs(nbit):
    N = 2 ** nbit
    remainder = 100 - (N % 100)
    Ntotal = N + remainder
    X = np.zeros((Ntotal, nbit))
    Y = np.zeros(Ntotal)

    for ii in xrange(Ntotal):
        i = ii % N

        for j in xrange(nbit):
            if i % (2**(j+1)) != 0:
                i -= 2**j
                X[ii, j] = 1
        Y[ii] = X[ii].sum() % 2
    return X, Y
