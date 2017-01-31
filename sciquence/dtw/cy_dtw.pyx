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

ctypedef double (*distance)(np.ndarray, np.ndarray)

def dtw(double[:, ::1] A, double[:, ::1]B, metric=None, int diaginal_margin=-1):
  '''
  Measure similarities between two sequences.

  When computing dtw distance, we perform following calculations:
  1. Compute distance matrix for given sequences A and B
  2. Find the warping path. We start from upper left corner (*point (0, 0)*)
    and trying to reach bottom right corner (*point (n_timesteps_A, n_timesteps_B)*)
    In every step we chose the next point minimizing total path cost.

  Parameters
  ----------
  A: np.ndarray
    A sequence
  B: np.ndarray
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


  References
  ----------
  .. [1] https://en.wikipedia.org/wiki/Dynamic_time_warping
  .. [2] Ratanamahatana Ch. A.,  Keogh E. (2004). ` Everything you know about Dynamic Time Warping is Wrong <http://wearables.cc.gatech.edu/paper_of_week/DTW_myths.pdf>_`

  '''

  cdef int i

  cdef np.ndarray[np.double_t, ndim=2] cost_mat
  cdef np.ndarray[np.int_t, ndim=2] traceback_mat

  #for i in range()




  # Traceback


  return [], 0
