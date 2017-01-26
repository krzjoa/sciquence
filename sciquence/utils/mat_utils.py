# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Matrix manipulation utils
# Author: Krzysztof Joachimiak
#
# License: MIT

import numpy as np


def diagonal_starts(A, R=1):
    '''


    Parameters
    ----------
    A
    R

    Returns
    -------

    '''
    Nx = A.shape[0]
    Ny = A.shape[1]

    diagonals = []

    #R=1

    lim1 = np.floor((Nx-1)/(2*R+1)).astype(int)  + 1
    lim2 = np.floor((Ny-1)/(2*R+1)).astype(int) + 1

    print lim1, lim2

    for i in xrange(0, lim1):
        diagonals.append(((2*R+1)*i, 0))

    for i in xrange(1, lim2):
        diagonals.append((0, (2*R+1)*i))

    return diagonals


# def diag_ends(A, diag_starts):
#
#     # FIXME: nie dziala!!!!
#     '''
#
#     Diagonal starts
#
#     Parameters
#     ----------
#     A
#     diag_starts
#
#     Returns
#     -------
#
#     '''
#     ends = []
#     min_diag = A.shape[1] - 1
#     #min_diag = max(A.shape) - 1
#     for s in diag_starts:
#         diff = abs(min_diag-max(s))
#         cross = min_diag if diff >= min_diag else diff
#         ends.append((s[0]+cross, s[1]+cross))
#     return ends



def diagonal_band(A, start, R):
    ln = max(A.shape) - 1
    min_len = min(A.shape)

    # Limits
    diff = abs(ln - max(start))


    # Prawidlowo!
    start_row = start[0] - R if start[0] - R >= 0 else 0
    end_row = start[0] + min_len + R+1 if start[0] + min_len + R < A.shape[0] else A.shape[0]

    print start_row, end_row

    # Poprawic warunek -R
    shift = 0 if start[0] <= start[1] else -R

    for i in xrange(start_row, end_row):
        start_col = max(0, start[1]-R+shift)
        end_col = min(A.shape[1], start[1]+R+shift+1)
        for j in xrange(start_col, end_col):
            print start_row, start_col, end_row, end_col
            A[i, j]=1
        shift += 1
    return A


# def find_diagonals(M, diag_margin=0):
#     '''
#
#     Find all the diagonals in the given matrix.
#     All the diagonals all at an angle 45 degree.
#
#     Parameters
#     ----------
#     M: ndarray
#         A numpy array
#     diagonal_window: int
#
#
#     Returns
#     -------
#     diagonals: list of tuple
#         Diagonals start and endings
#
#     '''
#     # TODO: Uproscic
#
#     diag_margin *= 2
#     if M.shape[0] == M.shape[1]:
#         return _fs_square(M, diagonal_window=diag_margin)
#     elif M.shape[0] > M.shape[1]:
#         return _fs_rows(M, diagonal_window=diag_margin)
#     else:
#         return _fs_cols(M, diagonal_window=diag_margin)
#
#
#  # Help functions
#
#
# def _fs_square(M, diagonal_window):
#     diagonals = []
#     # Above main
#     for i in xrange(0, len(M), diagonal_window+1):
#         start = (0, i)
#         end = (abs(len(M) - i - 1), len(M)-1)
#         diagonals.append([start, end])
#     # Below main diagonal
#     for i in xrange(diagonal_window+1, len(M), diagonal_window+1):
#         start = (i, 0)
#         end = (len(M)-1, abs(len(M)-1-i))
#         diagonals.append([start, end])
#     return diagonals
#
#
# def _fs_rows(M, diagonal_window):
#     diagonals = []
#
#     l_min = M.shape[1]
#
#     # Upper part
#     for i in xrange(0, l_min, diagonal_window + 1):
#         start = (0, i)
#         end = (abs(l_min - i - 1), l_min - 1)
#         diagonals.append([start, end])
#
#     # Central part
#     for i in xrange(diagonal_window+1, M.shape[0] - l_min, diagonal_window+1):
#         start = (i, 0)
#         end = (i + diagonal_window - 1 , len(M) - 1)
#         diagonals.append([start, end])
#
#     # Bottom part
#     for i in xrange(len(M)- l_min + 1, len(M), diagonal_window+1):
#         start = (i, 0)
#         end = (len(M)-1-diagonal_window, abs(len(M)-1-i-diagonal_window))
#         diagonals.append([start, end])
#     return diagonals
#
#
# def _fs_cols(M, diagonal_window):
#     diagonals = []
#
#     l_min = M.shape[0]
#
#     # Left part
#     for i in xrange(diagonal_window+1, l_min, diagonal_window+1):
#         start = (i, 0)
#         end = (l_min - 1, l_min - i -diagonal_window-1)
#         diagonals.append([start, end])
#
#     # Center part
#     for i in xrange(0, M.shape[1] - l_min, diagonal_window+1):
#         start = (0, i)
#         end = (l_min -1, i+l_min-1)
#         diagonals.append([start, end])
#
#     # Right part
#     for i in xrange(M.shape[1]-l_min, M.shape[1], diagonal_window+1):
#         start = (0, i)
#         end = (M.shape[0] - (i-l_min+1), M.shape[1] - 1)
#         diagonals.append([start, end])
#
#     return diagonals

