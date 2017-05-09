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
from sklearn.feature_extraction.text import TfidfVectorizer

from operator import add
from sciquence.sliding_window import wingen, raw_wingen
from sciquence.representation import sax

from scipy.spatial.distance import cosine
from sklearn.base import BaseEstimator



class SAX_VSM(BaseEstimator):
    '''

    Symbolic Aggregate Approximation - Vector Space Model classifier

    Parameters
    ----------
    window: int
        Length of sliding window
    word_length: int
        Number of PAA segments for every window in input sequence
    alphabet_size: int
        Number of quantization bins
    adjust: bool, default: True
        If True, computations are produced for all the windows

    References
    ----------
    .. [1] Pavel Senin, Sergey Malinchik (2013).,
            SAX-VSM: Interpretable Time Series Classification
           Using SAX and Vector Space Model
    .. [2] https://jmotif.github.io/sax-vsm_site


    '''

    def __init__(self, window, word_length=3, alphabet_size=5, adjust=True):

        # TODO: parametr word_length powinien być wielokrotnością parametru window
        # TODO: Check if scale it with global or local stddev and mean
        # TODO: Implement DIRECT
        # TODO: Improve performance
        # TODO: multiple time series for each class
        # TODO: write unit tests

        # Params
        self.window = window
        self.word_length = word_length
        self.alphabet_size = alphabet_size
        self.adjust = adjust

        # Inner objects
        self.tfidf = TfidfVectorizer()

        # Computed values
        self.timeseries = None


        # Inner objects
        # self.scaler = StandardScaler()


    def fit(self, X, y=None):
        rows = []
        for row in X:
            rows.append(self._transform(row))

        # TF-IDF transformation
        # TODO: implement own TF-IDF transformer. Here, some kind of hack is used
        hacky_list = [reduce(add, [word + " " for word in ts]) for ts in rows]

        self.timeseries =  self.tfidf.fit_transform(hacky_list)

        return self


    def predict(self, X):
        predictions = []
        # Transform and compute cosine similarity
        for row in X:
            pred = get_most_similar(self._transform(row), self.timeseries)
            predictions.append(pred)
        return np.array(predictions)


    def _transform(self, row):
        row_sax = []

        # TODO: check this option
        wgen = wingen if self.adjust else raw_wingen

        for window in wgen(row, self.window):
            row_sax.append(
                sax(window, window=self.word_length, alphabet_size=self.alphabet_size)
            )

        # Numerosity reduction
        row_sax = num_reduce(row_sax)
        return row_sax



# =============== UTILS ================ #

def num_reduce(words_sequence):
    out = []
    precedent = ""
    for word in words_sequence:
        if word != precedent:
            out.append(word)
        precedent = word
    return out


def get_most_similar(input_vec, all_classes):
    out = []
    for vec in all_classes:
        out.append(cosine(input_vec, vec))
    return np.argmax(out)