# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Author: Krzysztof Joachimiak
#
# License: MIT

#cython: boundscheck=False, wraparound=False

import numpy as np
cimport numpy as np


def segmental_dtw(np.ndarray A, np.ndarray B, int min_path_len=10,
                  int path_window=5, metic='cosine'):
  '''
  Find similarities between two sequences. Segmental DTW algorithm extends idea
  from Dynamic Time Warping method, and looks for the best warping path not only
  on the main diagonal, but also on the other. It facilitates performing not only
  the comparision of the whole sequences, but also discovering similarities
  between subsequences of given sequences A and B.

  Parameters
  ----------
  A: ndarray (n_samples, n_features)
    First sequence
  B: ndarray (n_samples, n_features)
    Second sequence
  min_path_len: int
    Minimal length of path
  metric: str or function
    Metric

  Returns
  -------
  matchings: list of list of tuple
      List of matching sequences

  See also
  --------
  DTW

  References
  ----------
  Park A. S. (2006).

  *Unsupervised Pattern Discovery in Speech:
  Applications to Word Acquisition and Speaker  Segmentation*

  https://groups.csail.mit.edu/sls/publications/2006/Park_Thesis.pdf

  '''
  cdef int N = len(A)
  cdef int M = len(B)
  cdef np.ndarray dist_mat

  # all_diags = all_diagonals(N-1, R=path_window)
  #
  # paths, costs = [], []
  # matchings = []
  # average = []
  #
  # for idx, path in enumerate(all_diags):
  #   start_i, start_j = path[0][0], path[0][1]
  #   end_i, end_j = path[1][0], path[1][1]
  #
  #   cost_mat, traceback_mat = dtw_distance(s, t, metric, start_i, start_j, end_i, end_j, path_window)
  #   path = traceback(start_i, start_j, end_i, end_j , traceback_mat)
  #
  #   if idx == inspect:
  #     paths.append(path)
  #     costs.append(cost_mat)
  #
  #   if len(path) >=path_len:
  #     bts, avg = max_avg_seq(distance_mat, path, path_len)
  #     matchings.append(bts)
  #     average.append(avg)

  # return matchings, average, costs, paths
