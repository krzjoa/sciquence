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
from sciquence.nn.neural_utils import init_weight

import numpy as np
from sklearn.utils import shuffle

import matplotlib.pyplot as plt

class TextGenerator(object):

    def __init__(self, D, M, V, learning_rate=10e-4, momentum=0.99,
                 reg=1., activation=T.tanh, epochs=10, show_fig=True):

        self.D = D # przestrzeń wektorowa opisująca
        self.M = M
        self.V = V

        self.momentum = momentum
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.show_fig = show_fig

        self.f = activation

        # Variables
        self.We = theano.shared(init_weight(V, D))
        self.Wx = theano.shared(init_weight(D, M))
        self.Wh = theano.shared(init_weight(M, M))
        self.bh = theano.shared(np.zeros(M))
        self.h0 = theano.shared(np.zeros(M))
        self.Wo = theano.shared(init_weight(M, V))
        self.bo = theano.shared(np.zeros(V))

        # Theano variables
        self.Xvar = T.ivector('X') # wektor indeksów
        self.Yvar = T.ivector('Y')

        self.params = [self.We, self.Wx, self.Wh, self.bh,
                       self.h0, self.Wo, self.bo]



    def fit(self, X):

        Ei = self.We[self.Xvar]

        def step(x_t, h_t1):

            h_t = self.f(x_t.dot(self.Wx) + h_t1.dot(self.Wh) + self.bh)
            y_t = T.nnet.softmax(h_t.dot(self.Wo) + self.bo)
            return h_t, y_t


        [h, y], _ = theano.scan(
            fn=step,
            outputs_info=[self.h0, None],
            sequences=Ei,
            n_steps=Ei.shape[0]
        )

        py_x = y[:, 0, :]
        prediction = T.argmax(py_x, axis=1)

        cost = -T.mean(T.log(py_x[T.arange(self.Xvar.shape[0], self.Yvar)]))
        grads = T.grad(cost, self.params)
        dparams = [theano.shared(p.get_value()*0) for p in self.params]

        updates = [
            (p, p + self.momentum * dp - self.learning_rate)
            for p, dp, g in zip(self.params, dparams, grads)
        ] + [
            (dp, self.momentum*dp - self.learning_rate*g)
            for dp, g in zip(dparams, grads)
        ]

        self.predict_op = theano.function([self.Xvar], prediction)
        self.train_op = theano.shared(
            [self.Xvar, self.Yvar],
            [cost, prediction],
            updates=updates
        )

        costs = []
        n_total = sum((len(sentence) + 1) for sentence in X)

        for i in xrange(self.epochs):
            X = shuffle(X)
            n_correct = 0
            cost = 0
            for j in xrange(self.N):
                input_sequence = [0] + X[j]
                output_sentence = X[j] + [1]

                c, p = self.train_op(input_sequence, output_sentence)
                cost += c

                for pj, xj in zip(p, output_sentence):
                    if pj == xj:
                        n_correct += 1
            print "i:", i, "cost:", "correct rate:", (float(n_correct) / n_total)
            costs.append(cost)

        if self.show_fig:
            plt.plot(costs)
            plt.show()


    def save(self, filename):
        np.savez(filename, *[p.get_value() for p in self.params])

    @staticmethod
    def load(filename, activation):
        npz = np.load(filename)
        We = npz['']
