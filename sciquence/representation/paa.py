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

    PAA is a method of time series representation.
    Every time point in the time series is quantized into the
    mean value in the given time range of length N.


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

    Examples
    --------
    >>> import numpy as np
    >>> from sciquence.representation import paa
    >>> np.random.seed(42)
    >>> random_time_series = np.random.rand(50)
    >>> print paa(random_time_series, window=10)
    [ 0.52013674  0.39526784  0.40038724  0.50927069  0.40455702]

    References
    ----------
    .. [1] https://jmotif.github.io/sax-vsm_site/morea/algorithm/PAA.html

    '''

    # TODO: Check adjust option
    # TODO: Consider optimization: output = np.zeros(len(sequence))

    wgen = wingen if adjust else raw_wingen

    output = []

    for w in wgen(sequence, window, window):
        output.append(np.mean(w))

    return np.array(output)

if __name__ == "__main__":
    from sax import sax
    np.random.seed(42)
    random_time_series = np.random.rand(50)
    print sax(random_time_series, window=10)