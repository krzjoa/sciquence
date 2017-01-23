# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Trace
# Author: Krzysztof Joachimiak
#
# License: MIT
#
#cython: boundscheck=False, wraparound=False

import numpy as np
cimport numpy as np
from libc.math cimport sqrt

cdef extern from "float.h":
    double DBL_MAX

def segmental_dtw(np.ndarray A, np.ndarray B, int min_path_len=10,
                  int diag_margin=5, str metric='cosine'):
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
  metric: str
    Metric name

  Returns
  -------
  matchings: list of list of tuple
      List of matching sequences

  See also
  --------
  dtw

  References
  ----------
  Park A. S. (2006).

  *Unsupervised Pattern Discovery in Speech:
  Applications to Word Acquisition and Speaker Segmentation*

  https://groups.csail.mit.edu/sls/publications/2006/Park_Thesis.pdf

  '''
  cdef int N = len(A)
  cdef int M = len(B)
  cdef int cost_mat, traceback_mat
  cdef list path

  cdef list all_diagonal_starts = diagonal_starts(N, M, diag_margin)
  cdef list best_path_fragments = []

  # Iterating all the diagonals
  for idx, diag_start in enumerate(all_diagonal_starts):
    # Computing costs on the diagonals
    cost_mat, traceback_mat = dtw_distance(A, B, diag_start, diag_margin, metric)
    print "Diagonal checked"
    # Traceback po optymalnej ścieżce
    #path = traceback(diag_start , traceback_mat)

    # if len(path) >=path_len:
    #   bts, avg = max_avg_seq(distance_mat, path, path_len)
    #   matchings.append(bts)
    #   average.append(avg)

  return N


  ########### Auxiliary functions ##############

cdef inline double cosine_dist(
        double[:, ::1] x, double[:, ::1] y, Py_ssize_t x_i, Py_ssize_t y_i
          ):
    """Calculate the cosine distance between `x[x_i, :]` and `y[y_i, :]`."""
    cdef int N = x.shape[1]
    cdef Py_ssize_t i
    cdef double dot = 0.
    cdef double norm_x = 0.
    cdef double norm_y = 0.
    for i in range(N):
        dot += x[x_i, i] * y[y_i, i]
        norm_x += x[x_i, i]*x[x_i, i]
        norm_y += y[y_i, i]*y[y_i, i]
      #return 1. - dot/(sqrt(norm_x) * sqrt(norm_y))
    return dot/(sqrt(norm_x) * sqrt(norm_y))

cdef inline double euclidean_dist(
        double[:, ::1] x, double[:, ::1] y, Py_ssize_t x_i, Py_ssize_t y_i
        ):
    """Calculate the Euclidean distance between `x[x_i, :]` and `y[y_i, :]`."""
    cdef int N = x.shape[1]
    cdef Py_ssize_t i
    cdef double sum_square_diffs = 0.
    for i in range(N):
        sum_square_diffs += (x[x_i, i] - y[y_i, i]) * (x[x_i, i] - y[y_i, i])
    return sqrt(sum_square_diffs)

  # Define a function pointer to a metric function
ctypedef double (*metric_ptr)(
    double[:, ::1], double[:, ::1], Py_ssize_t, Py_ssize_t
    )

cdef inline Py_ssize_t i_min3(double[3] v):
  cdef Py_ssize_t i, m = 0
  for i in range(1, 3):
    if v[i] < v[m]:
      m = i
    return m


def dtw_distance(np.ndarray A, np.ndarray B, tuple start, int R=1, str metric='cosine'):
  cdef int N, M, Nr
  cdef Py_ssize_t i_penalty

  cdef double[:, ::1] cost_mat
  cdef double[3] costs

  # Variables for controlling diagonal coordinates
  cdef int ln = max(A.shape[0], A.shape[1]) - 1
  cdef int min_len = min(A.shape[0], A.shape[1])

  cdef int start_row = start[0] - R if start[0] - R >= 0 else 0
  cdef int end_row = start[0] + min_len + R+1 if start[0] + min_len + R < A.shape[0] else A.shape[0]
  cdef shift = 0 if start[0] <= start[1] else -R

  cdef int i, j
  cdef int start_col, end_col

  cdef float dist

  cdef metric_ptr dist_func
  if metric == "cosine":
      dist_func = &cosine_dist
  elif metric == "euclidean":
      dist_func = &euclidean_dist
  else:
      raise ValueError("Unrecognized metric.")

  N = A.shape[0]
  M = B.shape[0]

  # Initialize the cost matrix
  cost_mat = np.zeros((N + 1, M + 1)) + DBL_MAX
  cost_mat[start[0], start[1]] = 0.

  # Fill the cost matrix
  traceback_mat = np.zeros((N, M), dtype=np.uint16)

  for i in xrange(start_row, end_row):
      start_col = max(0, start[1]-R+shift)
      end_col = min(A.shape[1], start[1]+R+shift+1)
      for j in xrange(start_col, end_col):
        dist = dist_func(A, B, i, j)
        costs[0] = cost_mat[i, j]       # match (0)
        costs[1] = cost_mat[i, j + 1]   # insertion (1)
        costs[2] = cost_mat[i + 1, j]   # deletion (2)
        i_penalty = i_min3(costs)
        traceback_mat[i, j] = i_penalty
        cost_mat[i + 1, j + 1] = dist + costs[i_penalty]
      shift += 1

  return cost_mat, traceback_mat
