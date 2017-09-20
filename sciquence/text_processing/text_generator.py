# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Text generator
# Author: Krzysztof Joachimiak
#
# License: MIT


import theano
import theano.tensor as T

class TextGenerator(object):

    def __init__(self, learning_rate=10e-4, momentum=0.99, reg=1.,
                 activation=T.tanh):



        # Variables
        self.We = None
