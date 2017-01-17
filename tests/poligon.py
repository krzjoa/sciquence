import numpy as np

#X = [['litwo', 'ojczyzno', 'moja'], ['ty', 'jestes', 'jak', 'zdrowie']]

#from operator import add

#print np.unique(reduce(add, X))

# we = WordEncoder()
#
# we.fit(X)
#
# z =  we.transform(X)
# print z
# print we.inverse_transform(z)
from sciquence.sliding_window import *

X_dummy = np.array(
    [1, 2, 3, 4, 5, 11, 12, 13, 14]
)

# Sliding window object
sw = SlidingWindow(window_size=3, shift=4)

print sw.transform(X_dummy)












