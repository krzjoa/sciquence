# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Searching in sequences
# Author: Krzysztof Joachimiak
#
# License: MIT

#cython: boundscheck=False, wraparound=False

import numpy as np
cimport numpy as np
cimport cython
from libc.stdlib cimport malloc, free
from cython.operator cimport postincrement as inc
from cython.operator cimport postdecrement as dec



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

    inc(i)
  return (mi, mj, ms)

# Longest segment algorithm

def longest_segment(np.ndarray sequence, float alpha):
  '''
  Find the longest subsequence which
  scores above a given threshold in O(n)

  Parameters
  ----------
  sequence: ndarray
    A sequence
  alpha: float
    Floating-point threshold being a lower bound for
    searched segment

  Returns
  -------
  segment: ndarray
    The longest segment with sum above given threshold

  Examples
  --------
  >>> from sciquence.sequences import longest_segment
  >>> import numpy as np
  >>> X = np.array([-1, -2, -3, -23, -45, -3, -4, 5, -56, 67, 1, 3, 4, 5])
  >>> ls1 = longest_segment(X, 30)
  >>> print ls1, sum(ls1)
  >>> [67  1  3  4  5] 80
  >>> # Next, we change -56 into -50
  >>> Z = np.array([-1, -2, -3, -23, -45, -3, -4, 5, -50, 67, 1, 3, 4, 5])
  >>> ls2 = longest_segment(Z, 30)
  >>> [ -4   5 -50  67   1   3   4   5] 31

  Notes
  -----
  Keep in mind that this algorithm maximizes segment length,
  not the segment total sum.

  References
  ----------
  Csűrös M. (2008).

  *A linear-time algorithm for finding the longest
  segment which scores above a given threshold*

  https://arxiv.org/pdf/cs/0512016.pdf

  '''
  # TODO: check memory usage

  cdef int n = len(sequence)
  cdef int N = n + 1

  cdef float* f = <float *> malloc(N * sizeof(float))
  cdef int i, j, k, m

  cdef int* l = <int *> malloc(N * sizeof(int))
  cdef int* r = <int *> malloc(N * sizeof(int))

  cdef float max = 0
  cdef np.ndarray segment = np.array([])

  # Prefix score
  f[0] = 0
  for i in range(1, N):
    f[i] = f[i-1] + sequence[i-1]
    #print "i", i, f[i]

  # Left sequence of minima
  k = 0
  l[0] = 0
  i = 0
  for i in range(1, N):
    if f[i] < f[l[k]]:
      inc(k)
      l[k] = i
      #print 'l', k, l[k]

  # Right sequence maxima
  m = 0
  r[0] = n
  for j in reversed(range(0, n)):
    if f[j] > f[r[m]]:
      inc(m)
      r[m] = j
      #print m

  # Finding max segment
  i = 0
  j = m

  while i <=k and j >= 0:
    while i <= k and f[l[i]] + alpha > f[r[j]]:
      inc(i)
    if i <= k:
      while j>= 0 and f[l[i]] + alpha <= f[r[j]]:
        if (r[j] - l[i]) > max:
          max = r[j] - l[i]
          segment = sequence[l[i]:r[j]]
        dec(j)

  return segment
