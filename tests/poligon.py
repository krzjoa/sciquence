import numpy as np


X = np.array([-1, -2, 600, -23, -45, -3, -4, 5, -50, 67, 1, 3, 4, 5])


Z = np.zeros((15, 5))

print Z.T


def find_diag_ends(M, diag_margin=1):
    diag_ends = []

    min_size = np.min(M.shape)
    max_size = np.max(M.shape)

    last_min = min_size - 1

    # Above main diagonal
    for i in xrange(0, M.shape[1], diag_margin+1):
        start = (0, i)
        end = (i + min_size - 1, i)
        #end = (abs(i-last_min), last_min)
        diag_ends.append([start, end])

    # Below main diagonal
    # for i in xrange(diag_margin+1, M.shape[0], diag_margin+1):
    #     start = (i, 0)
    #     end = ()
    #     diag_ends.append([start, end])


    return diag_ends

    #for col in xrange()


#print find_diag_ends(Z.T)

#
# def find_diagonals(M, diagonal_window=1):
#     diagonals = []
#
#     for i in xrange(0, M.shape[])







