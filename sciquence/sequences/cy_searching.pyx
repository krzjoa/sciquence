# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Searching in sequences
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np
cimport numpy as np
cimport cython
from libc.stdlib cimport malloc, free


@cython.boundscheck(False)
@cython.wraparound(False)
def mln_point(list A):
  '''

  MLN-Point algorith finds all left-negative pointers
  for a length n sequence in OðnÞ time

  References
  ----------
  Lin Y.L., Jiang T., Chaoc K.M. (2002)

  Efficient algorithms for locating the
  length-constrained heaviest segments
  with applications to biomolecular
  sequence analysis


  http://www.csie.ntu.edu.tw/~kmchao/papers/2002_jcss.pdf


  '''
  # FIXME: Reads out of bounds!

  cdef int n = len(A)
  cdef int i
  cdef int* p = <int *> malloc(n * sizeof(int))
  cdef int* w = <int *> malloc(n * sizeof(int))

  for i in reversed(range(0, n)):
    p[i] = i
    w[i] = A[i]
    while (p[i] < n) and w[i] <= 0:
       w[i] = w[i] + w[p[i] + 1]
       p[i] = p[p[i] + 1]
  try:
    return [ p[i] for i in range(n) ]
  finally:
    free(p)
    free(w)


@cython.boundscheck(False)
@cython.wraparound(False)
def mlsc(list A, int U):
  pass
