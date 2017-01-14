import numpy as np

from sciquence.load_utils import word2idx
#from sklearn.text_processing import LabelEncoder
#
#
# sen, w2i = word2idx('../data/pan-tadeusz.txt')
#
# print sen,
from sciquence.text_processing import WordEncoder


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

import sciquence.sequences.cy_searching as cys

x = np.array([9, -3, 1, 7,-15, 2, 3,-4, 2,-7, 6, -2, 8, 4, -9])
#print len(x)
#print cys.mln_point(list(x))

print x[0:2]

from sciquence.sequences import seq_equals

print seq_equals([np.array([1,2,3]), np.array([4,5,9])], [np.array([1,2,3]), np.array([4,5,6])])

#print cys.drs_point(list(x))
#print cys._d([1,2,3,4,5,6], 4)





