# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Recurrent neural network
# Author: Krzysztof Joachimiak
#
# License: MIT

import theano
import theano.tensor as T

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from neural_utils import init_weights, all_parity_pairs


class RecurrentLayer(object):

    def __init__(self, input_shape, num_units):

        # Sizes
        self.num_units = num_units
        self.input_shape = input_shape

        D = input_shape[-1] # Liczba ficzerów
        N = input_shape[0] # Liczba sekwencji wejściowych
        M = num_units
        K = 2 # Rozmiar wyjścia

        # Trainable params
        self.Wx = theano.shared(init_weights(D, M))                                        self.num_units))
        self.Wh = theano.shared(init_weights(M, M))
        self.bh = theano.shared(np.zeros(M))
        self.h0 = theano.shared(np.zeros(M))
        self.W0 = theano.shared(init_weights(M, K))