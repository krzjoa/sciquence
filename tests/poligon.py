import unittest
from sciquence.windows import WindowsMaker
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

x = [9,-3,1,7,-15,2,3,-4,2,-7,6,-2,8,4,-9]
print len(x)
print cys.mln_point(x)



