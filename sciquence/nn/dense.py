# -*- coding: utf-8 -*-

import theano
import theano.tensor as T
import numpy as np

class DenseLayer(object):

    def __init__(self, input_size, num_units):
        self.W = theano.shared(np.random.rand(input_size, num_units))
        self.b = theano.shared(np.random.rand(num_units))

        self.params = [self.W, self.b]

    def forward(self):
        pass

    def get_output_size(self):
        pass


