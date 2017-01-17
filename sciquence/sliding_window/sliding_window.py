# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Sliding window
# Author: Krzysztof Joachimiak
#
# License: MIT


from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import Imputer


class SlidingWindow(BaseEstimator, TransformerMixin):

    # TODO: check reference

    '''

    Class dedicated for simple sliding window transformations.
    It transforms only the one input sequence:
    for parallel X and y vectors processing see WindowsMaker

    Parameters
    ----------
    window_size: int, default 5
        Size of sliding window
    shift: int
        Shift of sliding window, default 1

    Attributes
    ----------
    window_size_: int
        Size of sliding window
    shift_: int
        Shift of sliding window

    Examples
    --------
    >>> from sciquence.sliding_window import SlidingWindow
    >>> import numpy as np
    >>> X = np.array([0, 1, 23, 3, 4, 67, 89, 11, 2, 34])
    >>> print SlidingWindow(window_size=3, shift=4).transform(X)
    >>> [array([1, 2, 3]), array([ 5, 11, 12])]

    References
    ----------
    Dietterich Thomas G.
    Machine Learning for Sequential Data: A Review

    http://web.engr.oregonstate.edu/~tgd/publications/mlsd-ssspr.pdf

    See Also
    --------
    WindowsMaker

    '''

    def __init__(self, window_size=5, shift=1):
        self.window_size_ = window_size
        self.shift_ = shift

    def fit(self, X, y=None):
        '''

        Mock method, does nothing.

        Parameters
        ----------
        X: ndarray (n_samples, n_features)
            A sequence

        Returns
        -------
        self: SlidingWindow
            Returns self

        '''
        return self

    def transform(self, X, y=None):
        # TODO: check array shape
        '''

        Transform sequence into sequence of contextual sliding_window

        Parameters
        ----------
        X: ndarray (n_samples, n_features)
            A sequence

        Returns
        -------

        '''
        windows = []
        range_end = len(X) - self.window_size_+1

        for i in xrange(0, range_end, self.shift_):
            windows.append(X[range(i, i+self.window_size_)])
        return windows



