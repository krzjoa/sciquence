#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Simple Recurrent Neural Networks in Theano
# Author: Krzysztof Joachimiak
#
# License: MIT

from sklearn.base import BaseEstimator
import theano
import theano.tensor as T
import numpy as np
from ..nn_utils import init_weights


class RNNGenerator(BaseEstimator):
    '''

    Simple Recurrent Neural Network

    '''
    def __init__(self, n_features, hidden_layer, vocabulary_size, learning_rate=10e-1,
                 mu=0.99, reg=1., activation=T.tanh, n_epochs=10):

        self.n_features = n_features # liczba wymmiarów
        self.hidden_layer = hidden_layer # Rozmiar warstwy ukrytej
        self.vocabulary_size = vocabulary_size

        # Training params
        self.activation = activation
        self.learning_rate = learning_rate
        self.mu = mu
        self.n_epochs = n_epochs
        self.reg = reg


    def fit(self, X, y=None):
        N = len(X)
        D = self.n_features
        M = self.hidden_layer
        V = self.vocabulary_size

        # initial weights
        We = init_weights((V,D))
        Wx = init_weights((D, M))
        Wh = init_weights((M, M))
        bh = np.zeros(M)
        h0 = np.zeros(M)
        z = np.ones(M)
        Wo = init_weights((M, V))
        bo = np.zeros(V)

        thX, thY, py_x, prediction = self.set(We, Wx, Wh, bh, h0, z, Wo, bo, self.activation)

        cost = -T.mean(T.log(py_x[T.arange(thY.shape[0]), thY]))
        grads = T.grad(cost, self.params)
        dparams = [theano.shared(p.get_value()*0) for p in self.params]

        updates = [
            (p, p + self.mu*dp - self.learning_rate for p, dp, g in zip(self.params, dparams))
        ]



