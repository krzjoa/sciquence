import numpy as np
from operator import itemgetter
import scipy.ndimage

def check_hit(tag, peaks):
    '''
    
    Return list of peaks which hit in specifc tag
    
    Parameters
    ----------
    tag: numpy.ndarray
        Tag (list of indices)
    peaks: list or numpy.ndarray
        List of peak indices

    Returns
    -------
    idx: list
        

    '''
    return list(set(tag).intersection(set(peaks)))


def multiwhere(elems, array_to_search):

    l = []
    for el in elems:
        found = np.where(array_to_search==el)[0]

        if len(found):
            l.append(found[0])

    return np.array(l)



def mark_percentage(tag):
    '''

    Return percentage markers for given tag

    Parameters
    ----------
    tag: numpy.ndarray
        Tag

    Returns
    -------
    percetage: numpy.ndarray
        Percentage

    '''
    perc = np.array(range(1, len(tag) + 1))
    perc = perc / float(len(tag))
    return perc


def mark_hits(tag, peaks):

    # Check hits
    hits = check_hit(tag, peaks)

    # Percentage
    perc = mark_percentage(tag)

    # Multiwhere
    idx = multiwhere(hits, tag)

    if len(idx):
        out = itemgetter(*idx)(perc)
        if not isinstance(out, tuple):
            return [out]
        else:
            return list(out)
    else:
        return []

def scale_binary_tag(col, output_size):
    '''
    
    Scale binary tagging
    
    Parameters
    ----------
    col: numpy.ndarray
        Numpy array with one/zero values only
    output_size: int
        Desired output size
            
    Returns
    -------
    scaled_tagging: numpy.ndarray
        Scaled tagging column
        
    Examples
    --------
    >>>  z = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0])
    >>>  print z.shape
    (19,)
    >>> print scale_binary_tag(z, 38)
    [0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0]

    '''
    scale = output_size / float(len(col))
    col = col.astype(int)
    return scipy.ndimage.zoom(col, scale)    
    
    
if __name__ == '__main__':

    a = np.array([1, 40, 45, 78, 67])

    b = np.array(range(39, 47))
    print b
    print "Multiwhere", multiwhere(a, b)
