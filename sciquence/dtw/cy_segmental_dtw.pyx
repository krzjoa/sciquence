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
from cython.operator import postincrement as inc


cdef extern from "float.h":
    double DBL_MAX

def segmental_dtw(np.ndarray A, np.ndarray B, int min_path_len=10,
                  int diag_margin=5, str metric='cosine'):
  '''
  Find similarities between two sequences.

  Segmental DTW algorithm extends ide  of Dynamic Time Warping method,
  and looks for the best warping path not only on the main diagonal,
  but also on the other. It facilitates performing not only
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

  # Limits
  cdef int N = len(A)
  cdef int M = len(B)
  cdef int i

  # Matrices
  cdef double[:, ::1] cost_mat
  cdef unsigned short[:, ::1] traceback_mat
  #cdef np.ndarray cost_mat, traceback_mat

  # TODO: optimize - distance should be added parallely,
  cdef double[:, ::1] dist_mat = distance_mat(A.astype(np.double), B.astype(np.double), metric=metric)
  cdef list path

  cdef list diag_starts = diagonal_starts(N, M, diag_margin)
  cdef list best_path_fragments = []

  cdef tuple end_point

  # Computing costs on the diagonals
  for i in range(len(diag_starts)):
    cost_mat, traceback_mat, end_point = dtw_distance(dist_mat, diag_starts[i], diag_margin, metric)

    # Traceback po optymalnej ścieżce
    path = traceback(diag_starts[i], end_point, traceback_mat)
    best_path_fragments.append(path)

    # Searching best fragments of paths
    # if len(path) >= min_path_len:
    #    bts, avg = mavs(distance_mat, path, min_path_len)
    #    best_path_fragments.append(bts)
      #average.append(avg)

  return best_path_fragments


########### Metrics ##############

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

############# Computing best diagonal paths ############

def dtw_distance(double[:, ::1] dist_mat, tuple start, int R=1, str metric='cosine'):

  cdef int N, M, Nr
  cdef Py_ssize_t i_penalty, i, j

  cdef double[:, ::1] cost_mat
  cdef double[3] costs

  N = dist_mat.shape[0]
  M = dist_mat.shape[0]

  # Initialize the cost matrix
  cost_mat = np.zeros((N + 1, M + 1)) + DBL_MAX
  cost_mat[start[0], start[1]] = 0.

  # Initialize traceback matrix
  traceback_mat = np.zeros((N, M), dtype=np.uint16)

  # Variables for controlling diagonal coordinates
  cdef int ln = max(dist_mat.shape[0], dist_mat.shape[1]) - 1
  cdef int min_len = min(dist_mat.shape[0], dist_mat.shape[1])

  cdef int start_row = start[0] - R if start[0] - R >= 0 else 0
  cdef int end_row = start[0] + min_len + R+1 if start[0] + min_len + R < dist_mat.shape[0] else dist_mat.shape[0]
  cdef int shift = 0 if start[0] <= start[1] else -R

  cdef int start_col, end_col

  for i in range(start_row, end_row):
      start_col = max(0, start[1]-R+shift)
      end_col = min(traceback_mat.shape[1], start[1]+R+shift+1)

      for j in range(start_col, end_col):
        dist = dist_mat[i, j]
        costs[0] = cost_mat[i, j]       # match (0)
        costs[1] = cost_mat[i, j + 1]   # insertion (1)
        costs[2] = cost_mat[i + 1, j]   # deletion (2)
        i_penalty = i_min3(costs)
        traceback_mat[i, j] = i_penalty
        cost_mat[i + 1, j + 1] = dist + costs[i_penalty]
      inc(shift)

  # Determining the end point
  e0 = end_row - 1 if end_row - 1 >=0 else 0
  e1 = end_col - 1 if end_col - 1 >=0 else 0

  return cost_mat, traceback_mat, (e0, e1)

########## Diagonal start points ##########

def diagonal_starts(int Nx, int Ny, int R=1):
  '''
  An auxillairy function based on equqtions mentioned in the
  "Unsupervised Pattern Discovery..."

  '''
  cdef int i, j

  cdef list diagonals = []

  cdef int lim1 = np.floor((Nx-1)/(2*R+1)).astype(int) + 1
  cdef int lim2 = np.floor((Ny-1)/(2*R+1)).astype(int) + 1

  for i in xrange(0, lim1):
      diagonals.append(((2*R+1)*i, 0))

  for j in xrange(1, lim2):
      diagonals.append((0, (2*R+1)*j))

  return diagonals

######### Computing distance matrix ##########

def distance_mat(double[:, ::1] s, double[:, ::1] t, str metric="cosine"):

  cdef int N, M, Nr
  cdef Py_ssize_t i, j

  cdef double[:, ::1] cost_mat
  cdef double[3] costs

  N = s.shape[0]
  M = t.shape[0]

  cdef metric_ptr dist_func
  if metric == "cosine":
      dist_func = &cosine_dist
  elif metric == "euclidean":
      dist_func = &euclidean_dist

  dist_mat = np.zeros((N, M))

  for i in range(N):
    for j in range(M):
      dist_mat[i, j] = dist_func(s, t, i, j)
  return dist_mat

############# Traceback ################

def traceback(start_point, end_point,  traceback_mat):
  i = end_point[0]
  j = end_point[1]
  cdef list path = [(i, j)]
  while i > start_point[0] or j > start_point[0]:
      tb_type = traceback_mat[i, j]
      if tb_type == 0:
          # Match
          i = i - 1
          j = j - 1
      elif tb_type == 1:
          # Insertion
          i = i - 1
      elif tb_type == 2:
          # Deletion
          j = j - 1
      path.append((i, j))
  return path

########## Maximal average sum ##########

# def mavs(dist_mat, path, seqlen):
#   cost_path = np.array([dist_mat[i[0], i[1]] for i in path])
#   i, j = search.max_avg_seq(cost_path, seqlen)
#   if i < len(path) and j < len(path):
#       fragment = np.array(path)[i:j+1]
#       print "Found path", len(fragment)
#       return fragment, np.mean(fragment)
#   else:
#       return [], []
