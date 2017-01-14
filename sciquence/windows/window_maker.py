# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Data processors for making windows
# Author: Krzysztof Joachimiak
#
# License: MIT

from sklearn.preprocessing import Binarizer


from ..base import Processor
import numpy as np


class WindowMaker(Processor):
    '''

    Object for making contextual windows in sequence/time series processing

    '''

    def __init__(self, window_size, shift=1, output_size='valid',
                 label_assigning='center', keep_features=False,  between=None):
        self.window_size = window_size
        self.shift = shift

        # Computed attributes
        self.margin = self.window_size // 2

    def process(self, X, y):
        new_x = []
        new_y = []
        for i in xrange(self.margin, len(X) - self.margin, self.shift):
            new_x.append(as_one_row(get_neighbourhood(X, i, self.margin)))
            new_y.append(y[i])
        return np.vstack(new_x), np.vstack(new_y)


def make_windows(x, y, window_size):
    new_x = []
    new_y = []
    margin = window_size / 2
    for i in xrange(margin, len(x)-margin):
        new_x.append(as_one_row(get_neighbourhood(x, i, margin)))
        new_y.append(y[i])
    return np.vstack(new_x), np.vstack(new_y)

def as_one_row(matrix):
    return np.hstack(np.vsplit(matrix, len(matrix)))

def get_neighbourhood(matrix, row, padding):
    return matrix[row-padding:row+padding+1]