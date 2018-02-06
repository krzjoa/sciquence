# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2018
# sciquence: Time series & sequences in Pythonn
#
# Binarizers
# Author: Krzysztof Joachimiak
#
# License: MIT

import sys
sys.path.append("..")

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import copy
#from sciquence.utils.docstring import inherit_docstring

#@inherit_docstring
class ClasswiseBinarizer(BaseEstimator, TransformerMixin):
    '''
    Performing binarization classwise. 
    
    It may be used for binarize independently multiple class in the tagging tasks.

    Parameters
    ----------
    thresholds: list of float or numpy.ndarray
        Binarization thresholds for all the classes
    
    '''
    def __init__(self, thresholds):
        # TODO: axis?
        self.thresholds=thresholds
        
    def fit(self, X, y=None):
        '''Does nothing'''
        return self
        
    def transform(self, X, y=None, copy=False):
       '''

       Perform classwise binarization, i.e. every column has
       own specific binarization thresholds.

       Parameters
       ----------
       X: numpy.ndarray
          Probabilities vector
       y: None
          Nothing, argument for API compatibility
       copy: bool
          Copy or make transformation inplace

       Returns
       -------
       binarized_X: numpy.ndarray
           Binarized output

       Examples
       ---------
       >>> import numpy as np
       >>> X = np.array(
       >>> [[ 0.04344385  0.24317802  0.81423947],
       >>> [ 0.30503777  0.08385118  0.48402043],
       >>> [ 0.38695257  0.64501778  0.19023201],
       >>> [ 0.49452506  0.35440145  0.74149338],
       >>> [ 0.25147325  0.14294654  0.6648142 ],
       >>> [ 0.99852846  0.75026559  0.43106003],
       >>> [ 0.33369685  0.41158767  0.86865335],
       >>> [ 0.07741532  0.90428353  0.87152301],
       >>> [ 0.79609158  0.47617837  0.1890651 ],
       >>> [ 0.14287567  0.52800364  0.10957203]]
       >>> )
       >>> X_binarized = ClasswiseBinarizer(thresholds=[.5, .4, .3]).transform(X)
       >>> print X_binarized
       >>> [[ 0.  0.  1.],
       >>> [ 0.  0.  1.],
       >>> [ 0.  1.  0.],
       >>> [ 0.  0.  1.],
       >>> [ 0.  0.  1.],
       >>> [ 1.  1.  1.],
       >>> [ 0.  1.  1.],
       >>> [ 0.  1.  1.],
       >>> [ 1.  1.  0.],
       >>> [ 0.  1.  0.]]

       '''
       return (X >= self.thresholds).astype(float)
       
       
def binarize_classwise(X, thresholds):
    '''
    
    Binarization performed classwise.

    Parameters
    ----------
    X: numpy.ndarray
        Probabilities vector
    thresholds: list of float or numpy.ndarray
        Binarization thresholds for all the classes

    Examples
    --------
    >>> import numpy as np
    >>> X = np.array(
    >>> [[ 0.04344385  0.24317802  0.81423947],
    >>> [ 0.30503777  0.08385118  0.48402043],
    >>> [ 0.38695257  0.64501778  0.19023201],
    >>> [ 0.49452506  0.35440145  0.74149338],
    >>> [ 0.25147325  0.14294654  0.6648142 ],
    >>> [ 0.99852846  0.75026559  0.43106003],
    >>> [ 0.33369685  0.41158767  0.86865335],
    >>> [ 0.07741532  0.90428353  0.87152301],
    >>> [ 0.79609158  0.47617837  0.1890651 ],
    >>> [ 0.14287567  0.52800364  0.10957203]]
    >>> )
    >>> X_binarized = ClasswiseBinarizer(thresholds=[.5, .4, .3]).transform(X)
    >>> print X_binarized
    >>> [[ 0.  0.  1.],
    >>> [ 0.  0.  1.],
    >>> [ 0.  1.  0.],
    >>> [ 0.  0.  1.],
    >>> [ 0.  0.  1.],
    >>> [ 1.  1.  1.],
    >>> [ 0.  1.  1.],
    >>> [ 0.  1.  1.],
    >>> [ 1.  1.  0.],
    >>> [ 0.  1.  0.]]
    
    '''
    return (X >= thresholds).astype(float)


## TODO: ClasswiseMeanBinarizer


if __name__== '__main__':

    # Dummy data
    X = np.random.rand(10, 3)

    print X

    # Binarizing
    bX = ClasswiseBinarizer(thresholds=[.5, .4, .3]).transform(X)

    print bX
