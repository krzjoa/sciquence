# -*- coding: utf-8 -*-
# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Pythonn
#
# Shapelet processor
# Author: Krzysztof Joachimiak
#
# License: MIT

from shapelet_utils import all_candidates
from sklearn.preprocessing import scale


class ShapeletProcessor(object):

    # TODO: add base classes and mixins

    def __init__(self, min, max):
        self.min = min
        self.max = max


    def fit(self, X, y):
        pass

    def fit_process(self, X, y):
        # Pass
        pass

    def process(self, X, y):
        pass








# def _shapelet_selection(multiple_ts, min, max):
#     # Best score & best shapelete
#     best = 0
#     best_shapelet = None
#
#     # TODO: optimize!
#     # First, highly unefficient implementation.
#     candidates = grouped_candidates(multiple_ts, min, max)
#
#     for Wl in candidates:
#         for S in Wl:
#             Ds = find_distances(S, Wl)
#             quality = asses_candidate(S, Ds)
#
#             if quality > best:
#                 best = quality
#                 best_shapelet = S
#
#     return best_shapelet
#
#
# # ============ UTILS ============ #
#
#
# def grouped_candidates(multiple_ts, min, max):
#     # Highly ineffcient!!!
#     W = []
#     for window_length in xrange(min, max + 1):
#         Wi = []
#         for time_series in multiple_ts:
#             ts_length = len(time_series)
#             for index in xrange(0, ts_length - window_length + 1):
#                 Wi.append(scale(time_series[index:index + window_length]))
#         W.append(Wi)
#     return W
#
#
# def find_distances(S, Wl):
#     pass
#
#
# def asses_candidate(S, Ds):
#     pass