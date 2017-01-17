import unittest
from sciquence.sliding_window import WindowMaker, SlidingWindow
from sciquence.sequences import seq_equals
import numpy as np


class TestWindowMaker(unittest.TestCase):


    def test_sliding_window(self):
        X_dummy = np.array(
            [1, 2, 3, 4, 5, 11, 12, 13, 14]
        )

        # Sliding window object
        sw = SlidingWindow(window_size=3)

        # Test 1
        expected1 = [
            np.array([1, 2, 3]),
            np.array([2, 3, 4]),
            np.array([3, 4, 5]),
            np.array([4, 5, 11]),
            np.array([5, 11, 12]),
            np.array([11, 12, 13]),
            np.array([12, 13, 14])
        ]

        assert seq_equals(sw.transform(X_dummy), expected1)

        # Test 2
        sw.shift_ = 3

        expected2 = [np.array([1, 2, 3]),
                     np.array([ 4,  5, 11]),
                     np.array([12, 13, 14])]

        assert seq_equals(sw.transform(X_dummy), expected2)


    def test_windows(self):

        X_dummy = np.array([
            [1, 2, 3, 4, 5],
            [11, 12, 13, 14, 15],
            [21, 22, 23, 24, 25]
        ])

        y_dummy = np.array([0, 1, 0])

        sw = WindowMaker(window_size=3)

        print sw.process(X_dummy, y_dummy)


if __name__ == '__main__':
    unittest.main()

