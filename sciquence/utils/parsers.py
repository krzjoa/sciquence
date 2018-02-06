# Krzysztof Joachimiak 2018
# sciquence: Time series & sequences in Python
#
# Matrix manipulation utils
# Author: Krzysztof Joachimiak
#
# License: MIT


class KwargsParser(object):
    '''
    
    Parsing keyword arguments
    
    '''

    def __init__(self, kwargs, default=None):
        self.kwargs = kwargs
        self.default = default

    def __getitem__(self, item):
        return self.get(item, default=self.default)

    def get(self, key, default=None):
        if key not in self.kwargs:
            return default
        else:
            return self.kwargs[key]
