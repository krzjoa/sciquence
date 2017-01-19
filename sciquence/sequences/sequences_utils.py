# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Functions for sequence processing
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
from itertools import groupby


def seq(array):
    '''

    Cut input array into sequences consisting of the same elements

    Parameters
    ----------
    array: ndarray
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of sequences

    '''
    return [np.array(list(group)) for elem, group in groupby(array)]


def specseq(array, element):
    '''

    Return sequences consisting of specific tag

    Parameters
    ----------
    array: ndarray
        Numpy array
    element: object
        Element

    Returns
    -------
    seq_list: list of ndarray
        List of sequences consisting of specific tag

    '''
    return [np.array(list(group)) for elem, group in groupby(array) if elem == element]



def nseq(array):
    '''

    Returns sequences consisting of zeros

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of negative sequences

    '''

    return [np.array(list(group)) for elem, group in groupby(array) if not elem]


def pseq(array):
    '''

    Returns sequences consisting of ones

    Parameters
    ----------
    array: array-like
        Numpy array

    Returns
    -------
    seq_list: list of ndarray
        List of positive sequences

    '''

    return [np.array(list(group)) for elem, group in groupby(array) if elem]



def seq_equals(lseqa, lseqb):
    '''

    Compare two lists of ndarrays

    Parameters
    ----------
    lseqa: list of ndarray
        List of sequneces
    lseqb: list of ndarray
        List of sequneces

    Returns
    -------
    ans: bool
        True if lists equal, otherwise False

    '''
    ans = [np.array_equal(a, b) for a, b in zip(lseqa, lseqb)]
    return np.logical_and.reduce(ans)


