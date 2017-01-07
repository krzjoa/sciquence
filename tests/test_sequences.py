import unittest
import numpy as np
from sciquence.sequences import seq, specseq


class TestSequences(unittest.TestCase):

    def test_seq(self):
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]
        assert np.all(seq(x)) == np.all(expected)

if __name__ == '__main__':
    unittest.main()

