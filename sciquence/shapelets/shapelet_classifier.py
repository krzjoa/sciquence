# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Pythonn
#
# Shapelet processor
# Author: Krzysztof Joachimiak
#
# License: MIT

from shapelet_utils import all_candidates
from sklearn.preprocessing import scale
from sklearn.base import BaseEstimator


class ShapeletClassifier(BaseEstimator):
    '''

    Shapelet tree-based classifier.

    Parameters
    ----------
    min: int
        Minimal length of window
    max: int
        Maximal length of window
    step: int
        Window step in process of looking for potential shapelets

    Examples
    --------
    >>> from sciquence.shapelets import ShapeletClassifier
    >>> from sklearn.model_selection import train_test_split
    >>> sc = ShapeletClassifier(min=5, max=10)
    >>> X, y = load_dataset()
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y)
    >>> prediction = sc.fit(X_train, y_train).predict(X_test, y_test)


    References
    ----------

    Ye L., Keogh E. (2009).

    Time Series Shapelets: A New Primitive for Data Mining

    http://alumni.cs.ucr.edu/~lexiangy/Shapelet/kdd2009shapelet.pdf

    '''

    def __init__(self, min, max):

        raise NotImplemented

        self.min = min
        self.max = max


    def fit(self, X, y):
        pass


    def predict(self, X):
        pass