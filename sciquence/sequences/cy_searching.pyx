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
from cython.operator cimport postincrement as inc


@cython.boundscheck(False)
@cython.wraparound(False)
def mln_point(list A):
  '''

  MLN-Point algorith finds all left-negative pointers
  for a length n sequence in O(n) time

  Parameters
  ----------
  A: list of float
    List of float numbers

  Returns
  -------
  ln_pointers: list of int
    List of left-negative pointers

  References
  ----------
  Lin Y.L., Jiang T., Chaoc K.M. (2002).

  Efficient algorithms for locating the
  length-constrained heaviest segments
  with applications to biomolecular
  sequence analysis

  http://www.csie.ntu.edu.tw/~kmchao/papers/2002_jcss.pdf

  '''

  cdef int n = len(A)
  cdef int i
  cdef int* p = <int *> malloc(n * sizeof(int))
  cdef int* w = <int *> malloc(n * sizeof(int))

  for i in reversed(range(n)):
    p[i] = i
    w[i] = A[i]
    # n-1 instead of n
    while (p[i] < n-1) and w[i] <= 0:
       w[i] = w[i] + w[p[i] + 1]
       p[i] = p[p[i] + 1]
  try:
    return ([ p[i] for i in range(n) ],
    [ w[i] for i in range(n) ])
  finally:
    free(p)
    free(w)


@cython.boundscheck(False)
@cython.wraparound(False)
def mslc(list A, int U):
  '''

  Given a length n real sequence,
  finds the consecutive subsequence of
  length at most U with the maximum sum in O(n) time.

  Parameters
  ----------
  A: list of float
    List of float numbers
  U: int
    Sum upper bound

  Returns
  -------
  ln_pointers: list of int
    List of left-negative pointers

  References
  ----------
  Lin Y.L., Jiang T., Chaoc K.M. (2002).

  Efficient algorithms for locating the
  length-constrained heaviest segments
  with applications to biomolecular
  sequence analysis

  http://www.csie.ntu.edu.tw/~kmchao/papers/2002_jcss.pdf

  '''

  # FIXME: memory error

  cdef int n = len(A) - 1
  cdef int i = 1
  cdef int ms, mi, mj
  cdef list p, w

  #j = 0

  while A[i] <=0 and i <= n:
    inc(i)
  if i == n:
    return [i, i, max(A)]

  # Compute mln_point(A)
  p, w = mln_point(A)
  j = i
  ms = 0
  while i <= n:
    while A[i] <= 0 and (i<=n):
      inc(i)
    j = max(i, j)
    print "max", i, j, max(i, j)
    while j < n and p[j+1] < i + U and w[j+i] > 0:
      j = p[j+1]
      print "Chuj"
    # if subseq_sum(i, j, A) > ms:
    #     mi = i
    #     mj = j
    #     ms = subseq_sum(i, j, A)
    #     print "upd", mi, mj, ms
    inc(i)
  return (mi, mj, ms)


@cython.boundscheck(False)
@cython.wraparound(False)
def subseq_sum(int i, int j, list A):
  return sum(A[i:j])
  # cdef int sum
  # for i in range(i, j+1):
  #   sum += A[i]
  # return sum
  #cdef int idx
  #pass

# @cython.boundscheck(False)
# @cython.wraparound(False)
# def drs_point(A):
#   '''
#
#   Sets up the right-skew pointers in O(n) time
#
#   Parameters
#   ----------
#   A: list of float
#     List of float numbers
#
#   Returns
#   -------
#   ln_pointers: list of int
#     List of right-skew pointers
#
#   References
#   ----------
#   Lin Y.L., Jiang T., Chaoc K.M. (2002).
#
#   Efficient algorithms for locating the
#   length-constrained heaviest segments
#   with applications to biomolecular
#   sequence analysis
#
#   http://www.csie.ntu.edu.tw/~kmchao/papers/2002_jcss.pdf
#
#   '''
#
#   cdef int n = len(A)
#   cdef int i
#   cdef int* p = <int *> malloc(n * sizeof(int))
#   cdef int* w = <int *> malloc(n * sizeof(float))
#   cdef int* d = <int *> malloc(n * sizeof(int))
#
#   for i in reversed(range(n)):
#     p[i] = i
#     w[i] = _w(A, i)
#     d[i] = _d(A, i)
#     while (p[i] < n-1) and (w[i]/d[i] <= w[p[i] + 1] /d[p[i] + 1]):
#         w[i] = w[i] + w[p[i] + 1]
#         d[i] = d[i] + d[p[i] + 1]
#         p[i] = p[p[i] + 1]
#   try:
#     return [ p[i] for i in range(n) ]
#   finally:
#      free(p)
#      free(w)
#      free(d)
#
# @cython.boundscheck(False)
# @cython.wraparound(False)
# def _w(list A, int idx):
#   print A, idx
#   return np.mean(A[idx:])
#
# @cython.boundscheck(False)
# @cython.wraparound(False)
# def _d(list A, int idx):
#     return len(A[idx:])
#
# @cython.boundscheck(False)
# @cython.wraparound(False)
# def max_avg_seq(A, L):
#   '''
#   Given a length n real sequence,
#   finding the consecutive subsequence of
#   length at least L with the maximum average
#   can be done in O(n log L) time.
#
#   Parameters
#   ----------
#   A: list of float
#     List of float numbers
#
#   Returns
#   -------
#   ln_pointers: list of int
#     List of right-skew pointers
#
#   References
#   ----------
#   Lin Y.L., Jiang T., Chaoc K.M. (2002).
#
#   Efficient algorithms for locating the
#   length-constrained heaviest segments
#   with applications to biomolecular
#   sequence analysis
#
#   '''
#   cdef int n = len(A)
#   cdef list p = drs_point(A)
#   cdef int i, j
#   cdef int* g = <int *> malloc(n * sizeof(int))
#
#   cdef list p = drs_point(A)
#
#   for i in range(n - L + 1):
#     j = i + L - 1
#     if mi(A, i, j) < mi(A, j+1, p[j+1]):
#       j = locate(A, p, i, j)
#     g[i] = j
#   return (i, g[i])
#
#
#
#
# @cython.boundscheck(False)
# @cython.wraparound(False)
# def mi(list A, int i, int j):
#   return np.mean(A[i:j+1])
#
# @cython.boundscheck(False)
# @cython.wraparound(False)
# def locate(list A, list p, int i, int j):
#   '''
#   Binary search
#
#   '''
#   cdef int k = np.ceil(np.log(L)).astype(int)
#
#   for i in reversed(range(k)):
#
#     if j >= n or (mi(i,j) >= mi(A, j+1, p[j+1]):
#       return j
#
#     if p
