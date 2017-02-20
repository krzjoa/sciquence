# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Transform
# Author: Krzysztof Joachimiak
#
# License: MIT

from ..base import Processor


import numpy as np

# TODO: optimize, tweak processor classes. Consider adding transformer classes.
#  Maybe functions should have arbitrary number of params

class RNNIput(Processor):

    def __init__(self, window_size, step=1, strategy='central'):
        self.window_size = window_size
        self.step = step
        self.strategy = strategy

    def fit_process(self, X, y):
        return super(RNNIput, self).fit_process(X, y)

    def fit(self, X, y):
        return super(RNNIput, self).fit(X, y)

    def process(self, X, y):
        return super(RNNIput, self).process(X, y)



class Seq2SeqInput(Processor):

    def __init__(self):
        pass

    def fit_process(self, X, y):
        return super(Seq2SeqInput, self).fit_process(X, y)

    def fit(self, X, y):
        return super(Seq2SeqInput, self).fit(X, y)

    def process(self, X, y):
        return super(Seq2SeqInput, self).process(X, y)


def _get_neighbourhood(matrix, row, padding):
    return matrix[row-padding:row+padding+1]

def rnn_input(X, y, window_size, step=1):
    # TODO: Add diffrent labeling strategies
    '''

    Prepare input for recurrent neural network.
    Input is prepared from two parallel time series:
    series of feature vectors and series of labels.

    Parameters
    ----------
    X: ndarray (time_series_length, n_features)
        A time series of feature vectors
    y: ndarray (time_series_length, )
        A time series of labels
    window_size: int
        Integer odd number
    step: int
        Step of sliding window

    Returns
    -------
    new_X: ndarray (n_samples, n_timesteps, n_features)
        Input for recurrent neural network
    new_y: ndarray (n_samples, )
        Time series of labels

    '''
    new_X = []
    new_y = []
    margin = window_size / 2
    for i in xrange(margin, len(X) - margin, step):
        neigh = _get_neighbourhood(X, i, margin)
        new_X.append(neigh.reshape(1, window_size, neigh.shape[1]))
        if y is not None: new_y.append(y[i])
    return np.vstack(new_X), np.vstack(new_y) if y is not None else None



def seq2seq_input(X, y, window_size, step=1, output_dim=1):
    # TODO: add examples, especially for output_dim usecase
    '''

    Prepare input for sequence2sequence recurrent neural network.
    Input is prepared from two parallel time series:
    series of feature vectors and series of labels.


    Parameters
    ----------
    X: ndarray (time_series_length, n_features)
        A time series of feature vectors
    y: ndarray (time_series_length, )
        A time series of labels
    window_size: int
        Integer odd number
    step: int
        Step of sliding window

    Returns
    -------
    new_X: ndarray (n_samples, n_timesteps, n_features)
        Input for recurrent neural network
    new_y: ndarray (n_samples, n_timesteps, output_dim)
        Time series of labels

    '''
    new_x = []
    new_y = []
    for i in xrange(0, len(X) - window_size+1, step):
        new_x.append(X[i:i + window_size].reshape(1, window_size, X.shape[1]))
        if y is not None: new_y.append(y[i:i+window_size].reshape(1, window_size, 1))
    return np.vstack(new_x), np.vstack(new_y) if y is not None else None










