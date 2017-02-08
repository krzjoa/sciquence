# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Functions for sequence processing
# Author: Krzysztof Joachimiak
#
# License: MIT

from sciquence.sliding_window import wingen, raw_wingen
import numpy as np


def paa(sequence, window, adjust=True):
    '''

    Piecewise Aggregate Approximation


    Parameters
    ----------
    sequence: ndarray (n_timesteps, 1)
        A sequence
    window: int
        Window length
    adjust: bool, default True
        Adjust size

    Returns
    -------
    paa_representation: ndarray
        PAA representation of input sequence

    References
    ----------
    .. [1] https://jmotif.github.io/sax-vsm_site/morea/algorithm/PAA.html

    '''

    wgen = wingen if adjust else raw_wingen

    output = []

    for w in wgen(sequence, window, window):
        output.append(np.mean(w))

    return np.array(output)
