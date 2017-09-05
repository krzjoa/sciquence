import unittest
import numpy as np
from sciquence.sequences import *


class TestSequences(unittest.TestCase):

    def test_seq_equals(self):
        x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        y = [np.array([1, 2, 7]), np.array([4, 5, 9])]
        assert lseq_equal(x, x)
        assert not lseq_equal(x, y)

    def test_seq(self):
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]

        assert lseq_equal(seq(x), expected)

    def test_specseq(self):
        x = np.array([2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]

        assert lseq_equal(specseq(x, element=2), expected)

    def test_nseq(self):
        ''' All the sequences consisting of zeros only'''
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([0, 0, 0, 0]), np.array([0, 0, 0])]

        assert lseq_equal(nseq(x), expected)

    def test_pseq(self):
        ''' All the sequences consisting of ones only'''
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([0, 0, 0, 0]), np.array([0, 0, 0])]

        assert lseq_equal(nseq(x), expected)

if __name__ == '__main__':
    unittest.main()

