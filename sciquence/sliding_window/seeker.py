# Krzysztof Joachimiak 2016
# sciquence: Time series & sequences in Python
#
# Classifying data fragments with sliding window
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
from sklearn.base import BaseEstimator
from sklearn.preprocessing import binarize
from sciquence.sliding_window import generate_windows


class Seeker(BaseEstimator):

    _estimator_type = "seeker"

    def __init__(self, estimator, train_pipeline=None,
                 test_pipeline=None, window_sizes=[3], windows_shifts=[1],
                 bin_threshold=0.5, proba_combiner=None):
        self.estimator_ = estimator
        self.train_pipeline = train_pipeline
        self.test_pipeline = test_pipeline
        self.window_sizes = window_sizes
        self.windows_shifts = windows_shifts
        self.bin_threshold = bin_threshold
        self.proba_combiner = proba_combiner

    def fit(self, X, y):
        '''

        Tranform train set with the train_pipeline and fit passed estimator

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Matrix containing data being a sequence or a time series.
        y : ndarray, shape (n_samples, )
            Labels for samples in the matrix X.

        Returns
        -------
        self : object,
            Return self.

        '''
        X, y = self.train_pipeline.fit_process(X, y)
        self.estimator_.fit(X, y)
        return self

    def predict_proba(self, X):
        # FIXME one sliding_window size only!!!
        #proba = np.zeros((len(X), ))
        raw_proba = []
        indices = []
        for fragment, idx in generate_windows(X, self.window_sizes[0], self.windows_shifts[0]):
            indices.append(idx)
            raw_proba.append(self.estimator_.predict(self.test_pipeline(fragment)))
        return self.proba_combiner.combine(raw_proba, indices, output_size=len(X))

    def predict_log_proba(self, X):
        return np.log(self.predict_proba(X))

    def predict(self, X):
        return binarize(self.predict_proba(X), threshold=self.bin_threshold)


