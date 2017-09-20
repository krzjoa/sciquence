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


def get_dparams(params):
    return [
        theano.shared(np.zeros(p.get_value().shape).astype(np.float32))
        for p in params
    ]


class RecurrentLayer(object):

    def __init__(self, input_shape, num_units, activation,
                 momentum=0.9, learning_rate=0.1, show_fig=True,
                 epochs=10):

        # Sizes
        self.num_units = num_units
        self.input_shape = input_shape
        self.epochs = epochs

        D = input_shape[-1] # Liczba ficzerów
        N = input_shape[0] # Liczba sekwencji wejściowych
        M = num_units
        K = 2 # Rozmiar wyjścia

        self.N = N

        self.f = activation
        self.momentum = momentum
        self.lr = learning_rate
        self.show_fig = show_fig
        self.epochs = epochs

        # Trainable params
        self.Wx = theano.shared(init_weights(D, M))
        self.Wh = theano.shared(init_weights(M, M))
        self.bh = theano.shared(np.zeros(M))
        self.h0 = theano.shared(np.zeros(M))
        self.Wo = theano.shared(init_weights(M, K))
        self.bo = theano.shared(np.zeros(K))

        self.params = [self.Wx, self.Wh, self.bh,
                       self.h0, self.Wo, self.bo]


    def fit(self, X, Y):

        Xvar = T.fmatrix('X')
        Yvar = T.ivector('Y')


        def step(x_t, h_t1):
            # Zwraca h(t), y(t)
            h_t = self.f(x_t.dot(self.Wx) + h_t1.dot(self.Wh) + self.bh)
            y_t = T.nnet.softmax(h_t.dot(self.Wo) + self.bo)
            return h_t, y_t

        # Theano scan
        [h, y], _ = theano.scan(
            fn=step,
            outputs_info=[self.h0, None],
            sequences=Xvar,
            n_steps=Xvar.shape[0]
        )

        py_x = y[:, 0, :]
        prediction = T.argmax(py_x, axis=1)

        cost = -T.mean(T.log(py_x[T.arange(Xvar.shape[0]), Yvar]))
        grads = T.grad(cost, self.params)
        dparams = get_dparams(self.params)

        updates = [
            (p, p + self.momentum * dp - self.lr*g)
            for p, dp, g in zip(self.params, dparams, grads)
        ] + [
            (dp, self.momentum * dp - self.lr*g)
            for dp, g in zip(dparams, grads)
        ]


        self.predict = theano.function(Xvar, prediction)

        self.train = theano.function(
            inputs=[Xvar, Yvar],
            outputs=[cost, prediction, y],
            updates=updates
        )

        costs = []

        for i in xrange(self.epochs):
            X, Y = shuffle(X, Y)
            n_correct = 0
            cost = 0
            for j in xrange(self.N):
                c, p, rout = self.train(X[j], Y[j])
                cost += c

                if p[-1] == Y[j, -1]:
                    n_correct += 1
            print "shape y:", rout.shape
            print "i:", i, "cost:", cost, "classification rate:", float(n_correct)
            costs.append(cost)

        if self.show_fig:
            plt.plot(costs)
            plt.show()


def parity(B=12, learning_rate=10e-5, epochs=200):
    X, Y = all_parity_pairs(B)
    N, t = X.shape

    Y_t = np.zeros(X.shape, dtype=np.int32)

    for n in xrange(N):
        ones_count = 0
        for i in xrange(t):
            if X[n, i] == 1:
                ones_count += 1
            if ones_count % 2 == 1:
                Y_t[n, i] = 1

    X = X.shape(N, t, 1).astype(np.float32)

    rnn = RecurrentLayer(X.shape)


if __name__ == '__main__':
    parity()