
import numpy as np


def generate_windows(X, window_size, step):
    last_index = len(X) - 1
    for index in xrange(0, len(X), step):
        ci = np.array(range(index, index + window_size))
        if ci[ci > last_index].size == 0:
            yield X[ci]