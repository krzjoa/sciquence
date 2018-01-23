

class KwargsParser(object):
    '''
    
    Parsing keyword arguments
    
    '''

    def __init__(self, kwargs):
        self.kwargs = kwargs

    def get(self, key, default=None):
        if key not in self.kwargs:
            return default
        else:
            return self.kwargs[key]
