import unittest
from sciquence.sliding_window import  SlidingWindow
from sciquence.sequences import lseq_equal
import numpy as np


class TestWindowMaker(unittest.TestCase):


    def test_sliding_window(self):
        pass
        # X_dummy = np.array(
        #     [1, 2, 3, 4, 5, 11, 12, 13, 14]
        # )
        #
        # # Sliding window object
        # sw = SlidingWindow(window_size=3)
        #
        # # Test 1
        # expected1 = [
        #     np.array([1, 2, 3]),
        #     np.array([2, 3, 4]),
        #     np.array([3, 4, 5]),
        #     np.array([4, 5, 11]),
        #     np.array([5, 11, 12]),
        #     np.array([11, 12, 13]),
        #     np.array([12, 13, 14])
        # ]
        #
        # assert lseq_equal(sw.transform(X_dummy), expected1)
        #
        # # Test 2
        # sw.shift_ = 3
        #
        # expected2 = [np.array([1, 2, 3]),
        #              np.array([ 4,  5, 11]),
        #              np.array([12, 13, 14])]
        #
        # assert lseq_equal(sw.transform(X_dummy), expected2)




if __name__ == '__main__':
    unittest.main()

