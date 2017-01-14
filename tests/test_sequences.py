import unittest
import numpy as np
from sciquence.sequences import *


class TestSequences(unittest.TestCase):

    def test_seq_equals(self):
        x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        y = [np.array([1, 2, 7]), np.array([4, 5, 9])]
        assert seq_equals(x, x)
        assert not seq_equals(x, y)

    def test_seq(self):
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]
        assert seq_equals(seq(x), expected)

if __name__ == '__main__':
    unittest.main()

