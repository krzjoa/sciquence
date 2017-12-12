# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Dynamic Time Warping
# Author: Krzysztof Joachimiak
#
# License: MIT
#
#cython: boundscheck=False, wraparound=False

# Inspired by: https://github.com/kamperh/speech_dtw
#             https://github.com/pierre-rouanet/dtw


import numpy as np
cimport numpy as np

# Pointer to function which returns
#ctypedef double (*distance)(np.ndarray, np.ndarray)

def dtw(A, B, metric):
  '''
  dtw(A, B, metric)
  
  Measure similarities between two sequences.

  When computing Dynamic Time Warping path, we are looking for the lowest cost
  path from (0, 0) to (len(A), len(B) point).

  Parameters
  ----------
  A: np.ndarray (a_rows, n_columns)
    A sequence
  B: np.ndarray (b_rows, n_columns)
    A sequence
  metric: function(np.ndarray, np.ndarray)
    A distance function with two parameters, which returns double

  Returns
  -------
  warping_path: list of tuple
    Points of warping path
  distance: double
    A distance between two sequences

  Examples
  --------
  >>> from sciquence.dtw import dtw
  >>> import numpy as np
  >>> from scipy.spatial.distance import cosine
  >>> A = np.random.rand(5, 3)
  >>> B = np.random.rand(8, 3)
  >>> warp_path, distance = dtw(A, B, cosine)

  References
  ----------
  .. [1] https://en.wikipedia.org/wiki/Dynamic_time_warping
  .. [2] Ratanamahatana Ch. A.,  Keogh E. (2004). ` Everything you know about Dynamic Time Warping is Wrong <http://wearables.cc.gatech.edu/paper_of_week/DTW_myths.pdf>_`

  '''

  # Margin of the diagonal search
  # TODO: check diagonal_margin size
  # TODO: Implement diagonal band costraints

  cdef Py_ssize_t i, j
  cdef int diag_margin = diag_margin
  cdef int N, M
  cdef double[3] costs

  N, M = A.shape[0], B.shape[0]

  cdef np.ndarray[np.double_t, ndim=2] cost_mat
  cdef np.ndarray[np.double_t, ndim=2] traceback_mat # Double, because of np.zeros output type

  # Initializing cost & traceback matrices filled with zeros
  cost_mat = np.zeros((N+1, M + 1)) + np.finfo(np.double).max
  traceback_mat = np.zeros((N, M))

  cost_mat[0, 0] = 0.

  # Filling cost_mat and traceback_mat
  for i in range(N):
    for j in range(M):
      costs = np.array([cost_mat[i, j], cost_mat[i, j+1], cost_mat[i+1, j]])
      lowest_cost_idx = np.argmin(costs)
      traceback_mat[i, j] = lowest_cost_idx
      cost_mat[i+1, j+1] = metric(A[i], B[j]) + costs[lowest_cost_idx]

  # Traceback
  path = _traceback(traceback_mat)

  return path, cost_mat[N, M]


def _traceback(traceback_mat):
  # TODO: set type

  cdef Py_ssize_t i, j
  i, j = traceback_mat.shape[0] - 1, traceback_mat.shape[1] - 1

  cdef path = [(i, j)]
  while i > 0 or j > 0:
    move = traceback_mat[i, j]

    if move == 0:
      i = i - 1
      j = j - 1
    elif move == 1:
      i = i - 1
    elif move == 2:
      j = j - 1
    path.append((i, j))

  return path
