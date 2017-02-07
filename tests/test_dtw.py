import unittest
import numpy as np
from sciquence.dtw import *
from scipy.spatial.distance import cosine


class TestDTW(unittest.TestCase):

    # TODO: extend unittest

    def test_dtw(self):
        A = np.random.rand(10, 12)
        B = np.random.rand(8, 12)
        path, dist = dtw(A, B, cosine)

        assert isinstance(dist, np.double)



if __name__ == '__main__':
    unittest.main()
