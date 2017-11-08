import unittest
import numpy as np
import sciquence.sequences as sq


class TestSequencesCutting(unittest.TestCase):

    def test_seq(self):
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]

        assert sq.lseq_equal(sq.seq(x), expected)

    def test_specseq(self):
        x = np.array([2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2])

        expected = [np.array([2, 2, 2]), np.array([2, 2, 2])]

        assert sq.lseq_equal(sq.specseq(x, element=2), expected)

    def test_nseq(self):
        ''' All the sequences consisting of zeros only'''
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([0, 0, 0, 0]), np.array([0, 0, 0])]

        assert sq.lseq_equal(sq.nseq(x), expected)

    def test_pseq(self):
        ''' All the sequences consisting of ones only'''
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([1, 1, 1]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([1, 1, 1, 1])]

        assert sq.lseq_equal(sq.pseq(x), expected)


    ############ SEQUENCE INDICES ############

    def test_seqi(self):
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]

        assert sq.lseq_equal(sq.seq(x), expected)

    def test_specseqi(self):
        x = np.array([2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2])

        expected = [np.array([1, 1, 1]), np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                    np.array([0, 0, 0, 0]), np.array([1, 1, 1, 1]), np.array([0, 0, 0])]

        assert sq.lseq_equal(sq.specseq(x, element=2), expected)

    def test_nseqi(self):
        ''' All the sequences consisting of zeros only'''
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([0, 0, 0, 0]), np.array([0, 0, 0])]

        assert sq.lseq_equal(sq.nseq(x), expected)

    def test_pseqi(self):
        ''' All the sequences consisting of ones only'''
        x = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0])

        expected = [np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                    np.array([0, 0, 0, 0]), np.array([0, 0, 0])]

        assert sq.lseq_equal(sq.pseq(x), expected)

if __name__ == '__main__':
    unittest.main()

