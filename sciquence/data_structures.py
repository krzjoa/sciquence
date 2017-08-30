

from collections import OrderedDict
from operator import itemgetter


class MultiDict(OrderedDict):

    ''
    A dictionary, which let you get multiple elements at once.
    
    ''

    def __getitem__(self, item):
        if isinstance(item, list):
            return itemgetter(*item)(self)
        else:
            return super(self.__class__, self).__getitem__(item)
