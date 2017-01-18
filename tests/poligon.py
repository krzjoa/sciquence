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

from sciquence.sliding_window import wingen

# X = np.array([[1, 2, 3],
#               [11, 12, 13],
#               [21, 22, 23],
#               [31, 32, 33]])
#
# print wingen(X, 2, 1).next()

from sciquence.sequences import longest_segment

x = np.array([-1, -2, -3, -23, -45, -3, -4, 5, -50, 67, 1, 3, 4, 5])

ls =  longest_segment(x, 30)
print  ls, sum(ls)










