# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Pythonn
#
# Shapelet utils
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def generate_candidates(time_series, min, max):
    ts_length = len(time_series)
    for window_length in xrange(min, max+1):
        for index in xrange(0, ts_length - window_length + 1):
            yield time_series[index:index+window_length]









if __name__ == "__main__":
    x = np.random.rand(50)
    gc = generate_candidates
    print x
    z = [ss for ss in gc(x, 2, 5)]
    print z



