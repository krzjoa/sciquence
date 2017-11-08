import numpy as np
import sciquence.sequences as sq

x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
            np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]

print sq.seq(x)
print sq.lseq_equal

#print sq.lseq_equal(sq.seq(x), expected)