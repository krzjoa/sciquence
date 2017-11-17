def parallel_filter(condition, *lists):
    '''
    
    Parallelly filter multiple lists.
    
    Parameters
    ----------
    condition: callable
        A function, which has as many arguments as the number of lists
    lists: list of list

    Returns
    -------
    filtered_lists:
        Filtered accordingly some criterion

    '''

    # TODO: check length

    if isinstance(lists[0], list) and len(lists) == 1:
        lists = lists[0]

    output = [[] for _ in xrange(len(lists))]

    for d in zip(*lists):
        if condition(*list(d)):
            multi_append(output, *list(d))
            print output

    return output
