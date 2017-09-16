# -*- coding: utf-8 -*-

import theano
import theano.tensor as T
import numpy as np

import lasagne

from neural_utils import init_weights

# TODO: poprawić


class InputLayer(object):

    def __init__(self, input_shape, input_var):
        self.input_shape = input_shape
        self.input_var = input_var

    def __call__(self, *args, **kwargs):
        return self.input_var

    def get_output(self, input=None):
        return self.input_var

    def forward(self):
        return self.input_var

    def get_output_size(self):
        return self.input_shape



class DenseLayer(object):

    # def __init__(self, incoming, num_units,
    #              nonlinearity=T.nnet.relu):

    def __init__(self, input_size, num_units,
                nonlinearity=T.nnet.relu):

        self.num_units = num_units

        # Params
        self.W = theano.shared(init_weights(input_size, num_units), name='W')
        self.b = theano.shared(np.zeros(num_units).astype(np.float32), name='b')

        self.params = [self.W, self.b]

        # Nonlinearity
        self.fun = nonlinearity

    def __call__(self, *args, **kwargs):

        model = args[0]

        return self.forward(model)


    def forward(self, input):
        if self.fun:
            return self.fun(input.dot(self.W) + self.b)
        else:
            return input.dot(self.W) + self.b


    # def get_output(self, input):
    #     if self.fun:
    #         return self.fun(input.dot(self.W) + self.b)
    #     else:
    #         return input.dot(self.W) + self.b
    #
    # def get_output_size(self):
    #     return self.num_units


def get_dparams(params):
    return [
        theano.shared(np.zeros(p.get_value().shape).astype(np.float32))
        for p in params
    ]


def forward_test():
    # Vector output len
    ln = 12

    # Getting data
    from neural_utils import all_parity_pairs
    X, Y = all_parity_pairs(ln)
    X = X.astype(np.float32)
    Y = Y.astype(np.float32)

    # Training hyperparams
    momentum = 0.9
    lr = 10e-5
    reg = 0.1
    batch_size = 32
    epochs = 300
    print_period = 10
    N, D = X.shape
    show_fig = True

    Xvar = T.matrix('X')
    Yvar = T.vector('Y')

    # Initializing layers
    input_layer = InputLayer(input_shape=(200, ln), input_var=Xvar)
    dense_1 = DenseLayer(input_size=D, num_units=2048)
    dense_2 = DenseLayer(input_size=2048, num_units=K)

    # Creating connections in graph
    model = input_layer()
    model = dense_1(model)
    model = dense_2(model)
    preds = T.nnet.softmax(model)
    #preds = preds.flatten()


    # Getting params
    params = dense_1.params + dense_2.params
    dparams = get_dparams(params)

    # Cost function
    rcost = reg*T.sum([(p**2).sum() for p in params])
    #cost = -T.mean(T.log(preds[T.arange(preds.shape[0]), preds])) + rcost

    cost = lasagne.objectives.binary_crossentropy(Yvar, preds)
    cost = cost.mean()  + rcost
    grads = T.grad(cost, params)

    updates = [
        (p, p + momentum*dp - lr*g) for p, dp, g in zip(params, dparams, grads)
    ] + [
        (dp, momentum*dp - lr*g)
        for dp, g in zip(dparams, grads)
    ]

    # Training function
    train_fun = theano.function(
        inputs=[Xvar, Yvar],
        outputs=[cost, preds],
        updates=updates
    )


    # Dummy data
    X = np.random.rand(200, ln).astype(np.float32)
    Y = np.random.rand(200, ).astype(np.float32)


    process = theano.function([Xvar, Yvar], [preds, cost])

    preds, cost = process(X, Y)

    print "Cost:", cost
    print "Preds:", preds.shape

    # process = theano.function([Xvar], preds)
    #
    # print process(X).shape


def training():
    # Vector output len
    ln = 12

    # Getting data
    from neural_utils import all_parity_pairs
    X, Y = all_parity_pairs(ln)
    X = X.astype(np.float32)
    Y = Y.astype(np.int32)
    #Y = Y.astype(np.float32)

    # Training hyperparams
    momentum = 0.9
    lr = 10e-5
    reg = 0.1
    batch_size = 32
    epochs = 300
    print_period = 10
    N, D = X.shape
    show_fig = True
    K = 2 # Binarne wyjście softmaxa

    Xvar = T.matrix('X')
    Yvar = T.ivector('Y')

    # Initializing layers
    input_layer = InputLayer(input_shape=(200, ln), input_var=Xvar)
    dense_1 = DenseLayer(input_size=D, num_units=2048)
    dense_2 = DenseLayer(input_size=2048, num_units=K)

    # Creating connections in graph
    model = input_layer()
    model = dense_1(model)
    model = dense_2(model)
    preds = T.nnet.softmax(model)
    #preds = preds.flatten()


    # Getting params
    params = dense_1.params + dense_2.params
    dparams = get_dparams(params)

    # Cost function
    rcost = reg*T.sum([(p**2).sum() for p in params])
    cost = -T.mean(T.log(preds[T.arange(preds.shape[0]), Yvar])) + rcost

    #cost = lasagne.objectives.binary_crossentropy(preds, Yvar)
    cost = cost.mean()  + rcost
    grads = T.grad(cost, params)

    updates = [
        (p, p + momentum*dp - lr*g) for p, dp, g in zip(params, dparams, grads)
    ] + [
        (dp, momentum*dp - lr*g)
        for dp, g in zip(dparams, grads)
    ]

    # Training function
    train_fun = theano.function(
        inputs=[Xvar, Yvar],
        outputs=[cost, preds],
        updates=updates
    )


    n_batches = N/ batch_size
    costs = []

    from sklearn.utils import shuffle
    import matplotlib.pyplot as plt

    for i in xrange(epochs):
        X, Y = shuffle(X, Y)

        print "Input", X.shape, Y.shape

        for j in xrange(n_batches):
            Xbatch = X[j*batch_size: (j*batch_size+batch_size)]
            Ybatch = Y[j*batch_size: (j*batch_size+batch_size)]

            c, p = train_fun(Xbatch, Ybatch)

            if j % print_period == 0:
                costs.append(c)
                e = np.mean(Ybatch != p)
                print "i: {}, nb: {}, costs: {}, error rate: {}".\
                    format(i, n_batches, c, e)

    if show_fig:
        plt.plot(costs)
        plt.show()



if __name__  == '__main__':
    training()



