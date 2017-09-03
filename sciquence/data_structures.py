# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Data structures
# Author: Krzysztof Joachimiak
#
# License: MIT

from collections import OrderedDict
from operator import itemgetter


class MultiDict(OrderedDict):

    '''

    A dictionary, which allows to get multiple elements at once

    Examples
    --------
    >>> md = MultiDict([('a', 1), ('b', 2), ('c', 3)])
    >>> print md[['c', 'a']]
    (3, 1)

    '''

    def __getitem__(self, item):
        if isinstance(item, list):
            return itemgetter(*item)(self)
        else:
            return super(self.__class__, self).__getitem__(item)
