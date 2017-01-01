import unittest
from sciquence.windows import WindowsMaker
import numpy as np






X_dummy = np.array([
            [1, 2, 3, 4, 5],
            [11, 12, 13, 14, 15],
            [21, 22, 23, 24, 25]
    ])

y_dummy = np.array([0, 1, 0])

wm = WindowsMaker(window_size=3)
print wm.process(X_dummy, y_dummy)