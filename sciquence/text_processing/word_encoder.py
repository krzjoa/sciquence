# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Word Encoder
# Author: Krzysztof Joachimiak
#
# License: MIT

from collections import OrderedDict
import numpy as np
from operator import add


class WordEncoder(object):
    '''

    Class used for for transforming text data into
    word indices

    '''

    def __init__(self):
        self.words = OrderedDict([('START',0), ('END',1)])

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.words.keys()[item]
        elif isinstance(item, str):
            return self.words[item]

    def fit(self, X, y=None):
        '''

        Fit WordEncoder object

        Parameters
        ----------
        X: list of list of str or str
            List containing list of strings or raw text input

        Returns
        -------
        self: object
            Returns self

        '''
        self.partial_fit(X)
        return self


    def partial_fit(self, X, y=None):
        '''

        Partially fit WordEncoder to the given word set

        Parameters
        ----------
        X: list of list of str or str
            List containing list of strings or raw text input

        Returns
        -------
        self: object
            Returns self

        '''
        unique = np.unique(reduce(add, X))
        current_index = len(self.words)
        update = [(word, current_index + idx)
                  for idx, word in enumerate(unique) if word not in self.words]
        self.words.update(update)
        return self


    def fit_transform(self, X, y=None):
        '''

        Fit WordEncoder and transform list of tokenized sentences
        (or raw text) into lists of indices

        Parameters
        ----------
        X: list of list of str or str
            List containing list of strings or raw text input

        Returns
        -------
        indices: list of list of int
            Nested list containing word indices

        '''
        return self.fit(X).transform(X)

    def transform(self, X, y=None):
        '''

        Transform list of tokenized sentences (or raw text) into lists of indices

        Parameters
        ----------
        X: list of list of str or str
            List containing list of strings or raw text input

        Returns
        -------
        indices: list of list of int
            Nested list containing word indices

        '''
        return [[self.words['START']] + [self.words[word]for word in sentence]
                +[self.words['END']] for sentence in X]

    def inverse_transform(self, X):
        ''''

        Transform list of indices into list of words

        Parameters
        ----------
        X: list of list of str or str
            List containing list of strings or raw text input

        Returns
        -------
        indices: list of list of int
            Nested list containing word indices


        '''
        return [[self.words.keys()[idx] for idx in sentence] for sentence in X]