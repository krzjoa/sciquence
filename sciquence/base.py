# Krzysztof Joachimiak 2016
# sciquence: Time series & sequences in Python
#
# Base classes
# Author: Krzysztof Joachimiak
#
# License: MIT

from sklearn.base import BaseEstimator
from abc import ABCMeta, abstractmethod
import six


class Processor(six.with_metaclass(ABCMeta, BaseEstimator)):

    '''

    Base class for parallel X and y transformations.
    Cannot be used directly, you can use only the derived classes.
    This class contains abstract methods

    '''

    _estimator_type = "processor"


    def fit(self, X, y):
        '''

        Check data characteristics

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Matrix containing data being a sequence or a time series.
        y : ndarray, shape (n_samples, )
            Labels for samples in the matrix X.

        Returns
        -------
        self : object,
            Return self.

        '''
        return self

    def process(self, X, y):
        '''

        Perform parallel transformation of X and y.

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Matrix containing data being a sequence or a time series.
        y : ndarray, shape (n_samples, )
            Labels for samples in the matrix X.

        Returns
        -------
        X_new: ndarray, shape (new_n_samples, new_n_features)
            Tranformed X matrix
        y_new : ndarray, shape (new_n_samples, )
            Labels for samples in the matrix the transformed matrix X.

        '''
        return X, y


    def fit_process(self, X, y):
        '''

        Check data characteristics and
        perform parallel transformation of X and y.

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Matrix containing data being a sequence or a time series.
        y : ndarray, shape (n_samples, )
            Labels for samples in the matrix X.

        Returns
        -------
        X_new: ndarray, shape (new_n_samples, new_n_features)
            Tranformed X matrix
        y_new : ndarray, shape (new_n_samples, )
            Labels for samples in the matrix the transformed matrix X.

        '''

        return self.fit(X, y).process(X, y)



#####################################################################


class Generator(six.with_metaclass(ABCMeta, BaseEstimator)):

    _estimator_type = "generator"

    @abstractmethod
    def fit(self, X, y=None):
        '''

        Parameters
        ----------
        X : ndarray, shape (n_samples, n_features)
            Matrix containing data being a sequence or a time series.

        Returns
        -------
        self: object
            Returns self

        '''

    @abstractmethod
    def generate(self, ln_seq):
        pass




#######################################################################


class Miner(six.with_metaclass(ABCMeta, BaseEstimator)):

    _estimator_type = "miner"