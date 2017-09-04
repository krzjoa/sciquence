



def parallel_sort(*arrays):
    '''
    
    Parallel sort. It always uses values from the first array 
    to sort all them.
    
    lists: lists or/and ndarrays
        Numpy arrays (at least one)
    
    '''
    first_array = arrays[0]

    print "first array", first_array.ndim

    # First array should be one-dimensional
    if arrays[0].ndim != 1:
        raise Exception("Number of dimensions different than 1!")

    # Check, if all the arrays have the same size
    # compare_shapes()

    # Sorting indices
    idx = range(0, len(arrays[0]))
    sorted_values, sorted_idx = zip(*sorted(zip(arrays[0], idx)))
    sorted_idx = list(sorted_idx),

    return [arr[sorted_idx] for arr in arrays]
