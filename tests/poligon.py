import numpy as np
# from sciquence.utils import diagonal_starts, diagonal_band
# from sciquence.dtw import segmental_dtw
#
#
# #X = np.array([-1, -2, 600, -23, -45, -3, -4, 5, -50, 67, 1, 3, 4, 5])
#

#Z = np.zeros((101, 129))

# print Z
#
# ds = diagonal_starts(Z, 1)
#
# for i in ds:
#     print diagonal_band(Z, i, 5)
#
# print ds

# from sciquence import sequences as sq
# x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
# print sq.specseq(x, 44)

# def find_diag_ends(M, diag_margin=1):
#     diag_ends = []
#
#     min_size = np.min(M.shape)
#     max_size = np.max(M.shape)
#
#     last_min = min_size - 1
#
#     # Above main diagonal
#     for i in xrange(0, M.shape[1], diag_margin+1):
#         start = (0, i)
#         end = (i + min_size - 1, i)
#         #end = (abs(i-last_min), last_min)
#         diag_ends.append([start, end])
#
#     # Below main diagonal
#     # for i in xrange(diag_margin+1, M.shape[0], diag_margin+1):
#     #     start = (i, 0)
#     #     end = ()
#     #     diag_ends.append([start, end])
#
#
#     return diag_ends
#
#     #for col in xrange()


#print find_diag_ends(Z.T)

#
# def find_diagonals(M, diagonal_window=1):
#     diagonals = []
#
#     for i in xrange(0, M.shape[])


# x = [1,2,3,4,5]
#
# sl = slice(1, 5, 2)

from sciquence.dtw import dtw
from scipy.spatial.distance import cosine

A = np.random.rand(5, 3)
B = np.random.rand(8, 3)

print A, B

print dtw(A, B, cosine)