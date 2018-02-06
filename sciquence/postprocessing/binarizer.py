# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2018
# sciquence: Time series & sequences in Pythonn
#
# Binarizers
# Author: Krzysztof Joachimiak
#
# License: MIT



import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class ClasswiseBinarizer(BaseEstimator, TransformerMixin):
    '''
    Performing binarization classwise. 
    
    It may be used for binarize independtly multiple class in the tagging tasks.
    
    '''
    def __init__(self, thresholds):
        self.thresholds=thresholds
        
    def fit(self, X, y=None)
        '' Does nothing ''
        return self
        
    def transform(self, X, y=None, copy=False):
       return (X >= self.thresholds).astype(float)
       
       

class ClasswiseMeanBinarizer(BaseEstimator, TransformerMixin):
    '''
    Performing binarization classwise. 
    
    It may be used for binarize independtly multiple class in the tagging tasks.
    
    '''
    def __init__(self):
        self.thresholds=thresholds
        
    def fit(self, X, y=None)
        '' Does nothing ''
        return self
        
    def transform(self, X, y=None, copy=False):
       return (X >= self.thresholds).astype(float)




def binarize_classwise(X, thresholds):
    '''
    
    Binarizization perforemed classwise.
    
    '''
    return (X >= thresholds).astype(float)
