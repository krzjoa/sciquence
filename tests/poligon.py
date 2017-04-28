import sciquence.sequences as sq
import numpy as np
# x = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 44, 44, 44, 44, 44, 1, 1, 0, 0, 0, 0])
# print sq.seqi(x)


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print sq.chunk(x, 3)