# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Sequence conversion
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def to_idx(sl, as_array=False):
    '''

    Convert slice object to list of indices

    Parameters
    ----------
    sl: slice
        A slice object with given range
    as_array: bool, default False


    Returns
    -------
    idx:

    '''
    if as_array:
        return np.array(range(sl.start, sl.stop, sl.step))
    return range(sl.start, sl.stop, sl.step)