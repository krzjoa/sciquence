#!python
#cython: boundscheck=False, wraparound=False, cdivision=True

import numpy as np
cimport numpy as np
cimport cython
from libc.stdlib cimport malloc, free
from cpython cimport bool
from operator import itemgetter
from libc.math cimport sqrt

# Metrics

# Define a function pointer to a metric function
ctypedef double (*metric_ptr)(
    double[:, ::1], double[:, ::1], Py_ssize_t, Py_ssize_t
    )

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


def calculate_ig(list objects):
  '''

  Implements subroutine "CalculateInformationGain"

  '''
  cdef float osp = optimal_split_point(objects)
  return (info_gain(objects, osp), osp)


def optimal_split_point(list objects):
  '''
  Compute optimal split point of given two-class dataset.

  Parameters
  ----------
  objects: list of tuple (object_index, distance_value, class)
    List of time series with distances from a given shapelet
  '''
  cdef int i
  cdef float split_point
  cdef list possible_sp = []

  # TODO: Optimize to avoid sorting
  # Sorting objects to calculate an optimal split point
  objects.sort(key=lambda d:d['value'])

  # Searching for optimal spllit point
  for i in range(0, len(objects)-1):
    split_point = np.mean([objects[i]['value'], objects[i+1]['value']])
    ig = info_gain(objects, split_point)
    possible_sp.append((split_point, ig))

  return max(possible_sp, key=itemgetter(1))[0]


def entropy(int A, int B, int all):
  cdef float class_a = float(A)
  cdef float class_b = float(B)
  cdef float total_count = float(all)

  cdef float pA = class_a / total_count
  cdef float pB = class_b / total_count

  cdef float logpB, logpA

  # Logarithms
  if pB == 0:
    logpB = 1
  else:
    logpB = np.log(pB)

  if pA == 0:
    logpA = 1
  else:
    logpA = np.log(pA)

  return (-1) * pA * logpA - pB * logpB


def subseq_dist_ea(np.ndarray T, np.ndarray S, str metric='cosine'):
  '''

  Early abandon the non-minimum distance


  References
  ----------

  Ye L., Keogh E. (2009.)

  Time Series Shapelets: A New Primitive for Data Mining

  http://alumni.cs.ucr.edu/~lexiangy/Shapelet/kdd2009shapelet.pdf

  '''
  cdef float min_dist = np.finfo(float).max
  cdef float sum_dist
  cdef bool stop = False
  cdef int n = len(T) - len(S) + 1
  cdef int ns = len(S)
  cdef int i, k
  cdef np.ndarray ST

  cdef int best_seq = 0

  # Metric selection
  cdef metric_ptr dist_func

  if metric == "cosine":
      dist_func = &cosine_dist
  elif metric == "euclidean":
      dist_func = &euclidean_dist
  else:
      raise ValueError("Unrecognized metric.")


  # For each subsequence S from T of length |S|
  for i in range(n):
    stop = False
    ST = T[i:i+ns]
    sum_dist = 0.

    for k in range(ns):
      #sum_dist += np.square(ST[k] - S[k])
      dist = dist_func(ST, S, k, k) #* 100
      sum_dist += dist

      #print "Sum_dist", sum_dist, min_dist

      if sum_dist >= min_dist:
        stop = True
        break

    if not stop:
      min_dist = sum_dist
      best_seq = i

  return min_dist, best_seq


def info_gain(list histogram, float split_point):

  '''

  Compute information gain basing on spectrogram

  Parameters
  ----------
  histogram: list of dict {'value':v, 0:n_1, 1: n_1}
      Ordered list of hsitogram bins
  split_point: float
      A point splitting dataset into two categories

  Returns
  -------
  information_gain: float
      Information gain

  '''
  cdef np.ndarray classes = np.zeros((2,))
  cdef np.ndarray conf_mat = np.zeros((2,2))
  cdef int i
  cdef float Id, d1, d2

  # Checking classes quantity
  for i in range(len(histogram)):
    current = histogram[i]
    classes[0] += current[0]
    classes[1] += current[1]

    # Class 1
    conf_mat[0, 0] += current[0] if current['value'] < split_point else 0
    conf_mat[1, 0] += current[1] if current['value'] < split_point else 0

    # Class 2
    conf_mat[1, 1] += current[1] if current['value'] >= split_point else 0
    conf_mat[0, 1] += current[0] if current['value'] >= split_point else 0

  # Compute entropy
  Id = entropy(classes[0], classes[1], np.sum(classes))
  d1_sum = np.sum(conf_mat[:, 0])
  d1 = (d1_sum / np.sum(classes)) * entropy(conf_mat[0, 0], conf_mat[1, 0], d1_sum)

  d2_sum = np.sum(conf_mat[:, 1])
  d2 = (d2_sum / np.sum(classes)) * entropy(conf_mat[1, 1], conf_mat[0, 1], d2_sum)

  return Id - (d1 + d2)

# Cython classifier
