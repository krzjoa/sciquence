# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Statistic utils
# Author: Krzysztof Joachimiak
#
# License: MIT

import scipy.stats


def gaussian_breakpoints(n_ranges):
    '''

    Get quantiles of Gaussian distribution.

    Parameters
    ----------
    n_ranges: int
        Number of equal ranges in Gaussian distribution

    Returns
    -------
    breakpoints: list of float
        List of Gaussian quantiles

    '''
    quantile_range = 1. / n_ranges
    quantiles = [quantile_range*i for i in range(1, n_ranges)]
    return [round(scipy.stats.norm.ppf(q), 2) for q in quantiles]