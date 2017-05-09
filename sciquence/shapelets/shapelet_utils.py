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


def all_candidates(multiple_ts, min, max):
    for ts in multiple_ts:
        yield generate_candidates(ts, min, max)


def grouped_candidates(multiple_ts, min, max):
    # Highly ineffcient!!!
    W = []
    for window_length in xrange(min, max + 1):
        Wi = []
        for time_series in multiple_ts:
            ts_length = len(time_series)
            for index in xrange(0, ts_length - window_length + 1):
                Wi.append(time_series[index:index + window_length])
        W.append(Wi)
    return W



if __name__ == "__main__":
    x = np.random.rand(50)
    gc = generate_candidates
    print x
    z = [ss for ss in gc(x, 2, 5)]
    print z



