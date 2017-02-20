# Krzysztof Joachimiak 2017
# sciquence: Time series & sequences in Python
#
# Symbolic Aggregate Approximation
# Author: Krzysztof Joachimiak
#
# License: MIT

from .paa import paa


def sax(sequence, window, adjust=True):
    '''


    Returns
    -------

    References
    ----------
    .. [1] http://www.cs.ucr.edu/~eamonn/SAX.htm
    .. [2] https://jmotif.github.io/sax-vsm_site/morea/algorithm/SAX.html

    '''

    # First step: PAA transformation


