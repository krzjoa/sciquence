# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Recurrent neural network
# Author: Krzysztof Joachimiak
#
# License: MIT



class RecurrentLayer(object):

    def __init__(self, incoming, num_units):
        self.num_units = num_units