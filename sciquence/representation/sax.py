# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Symbolic Aggregate Approximation
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
import scipy.stats
from sklearn.preprocessing import scale, StandardScaler

from paa import paa
from operator import add


def sax(sequence, window, alphabet_size=5, adjust=True):
    '''

    Symbolic Aggregate Approximation.

    Transform time series into a string.

    Parameters
    ----------
    sequence: numpy.ndarray
        One-dimensional numpy array of arbitrary length
    window: int
        Length of sliding window
    alphabet_size: int
        Number of Gaussian breakpoints
    adjust: bool, default True
        Compute only for equal-size chunks

    Returns
    -------
    sax_representation: str
        A SAX representation

    Examples
    --------
    >>> import numpy as np
    >>> from sciquence.representation import sax
    >>> np.random.seed(42)
    >>> random_time_series = np.random.rand(50)
    >>> print sax(random_time_series, 10, alphabet_size=5)
    dcccc

    References
    ----------
    .. [1] Lin, J., Keogh, E., Lonardi, S., & Chiu, B. (2003).
           A Symbolic Representation of Time Series,
           with Implications for Streaming Algorithms.
           In proceedings of the 8th ACM SIGMOD Workshop
           on Research Issues in Data Mining and Knowledge Discovery.

           http://www.cs.ucr.edu/~eamonn/SAX.pdf

    .. [2] http://www.cs.ucr.edu/~eamonn/SAX.htm
    .. [3] https://jmotif.github.io/sax-vsm_site/morea/algorithm/SAX.html

    '''

    # TODO: check dimensionality, size, aphabet size etc.
    # Pre-step: checking if all arguments have proper values


    # First step: Standardization ( aka normalization, z-normalization or standard score)
    scaled = scale(sequence)

    # Second step: PAA
    paa_repr = paa(scaled, window=window, adjust=adjust)

    # Last step:
    breakpoints = gauss_breakpoints(alphabet_size)
    letters = _alphabet(alphabet_size)

    breakpoints= np.array(breakpoints)
    symbols = np.array(letters)
    return reduce(add, symbols[np.digitize(paa_repr, breakpoints)])


# =========== SAX object ============ #
# TODO: consider: some classes should be both transformers and processors

class SAX(object):

    def __init__(self, n_ranges=5, keep_scale=True):
        self.scaler = StandardScaler()
        self.breakpoints = gauss_breakpoints(n_ranges)

    def fit(self, X, y):
        return self


    def transform(self, X, y):
        pass

    def fit_transform(self, X, y):
        return self.fit(X, y).transform(X, y)


# ================ UTILS ================ #


def gauss_breakpoints(n_ranges):
    # TODO: move this function to utilities
    '''

    Get quantiles of Gaussian distribution.

    Parameters
    ----------
    n_ranges: int
        Number of equal ranges in Gaussian distribution

    Returns
    -------
    breakpoints: list of float
        List of Gaussian quantiles

    '''
    quantile_range = 1. / n_ranges
    quantiles = [quantile_range*i for i in range(1, n_ranges)]
    return [round(scipy.stats.norm.ppf(q), 2) for q in quantiles]

def _alphabet(n_letters):
    import string
    return np.array(list(string.ascii_lowercase)[:n_letters])


def get_bins(sequence, breakpoints, symbols):
    breakpoints= np.array(breakpoints)
    symbols = np.array(symbols)
    return np.digitize(sequence, breakpoints)[symbols]


if __name__ == '__main__':
    # rts = np.random.rand(20)*10
    # saxed = sax(rts, 3)
    # print saxed
    #print gauss_breakpoints(10)
    #import scipy.stats
    #print scipy.stats.norm.ppf(1. / 3)

    random_ts = np.random.rand(30, 100)
    print random_ts
