# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Searching in sequences, part 2
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



def max_seq(A):
  '''

  Find all maximal scoring subsequences.
  Time: O(n)

  Parameters
  ----------
  A: ndarray
    A sequence

  Returns
  -------
  max_score_seq: list of ndarray
      List of maximal scoring subsequences

  Examples
  --------
  >>> import numpy as np
  >>> import sciquence.sequences as sq
  >>> x = np.array([4, -5, 3, -3, 1, 2, -2, 2, -2, 1, 5])
  >>> print sq.max_seq(x)

  References
  ----------
  Ruzzo W. L., Tompa M. (1999)
  A Linear Time Algorithm for Finding All Maximal Scoring Subsequences
  https://homes.cs.washington.edu/~ruzzo/papers/maxseq.pdf

  '''
  #TODO: optimize!

  cdef float accum = 0.
  cdef list max_seq = []
  cdef list lr_pairs = []
  cdef int i
  cdef float current_number, L, R

  # First step: completing list
  print "Len A", len(A)


  current_subseq = []
  current_pair = []

  for i in range(len(A)):
    current_number = A[i]

    # Appending L
    if len(current_pair) == 0:
      current_pair.append(accum)

    if current_number < 0:
      max_seq.append(current_subseq)
      current_pair.append(accum+current_number)
      lr_pairs.append(current_pair)
      current_subseq = []
      current_pair = []
    elif i == len(A)-1:
      current_subseq.append(current_number)
      max_seq.append(current_subseq)
      current_pair.append(accum+current_number)
      lr_pairs.append(current_pair)
      current_pair = []
    else:
      current_subseq.append(current_number)

      accum += current_number

  return max_seq, lr_pairs
