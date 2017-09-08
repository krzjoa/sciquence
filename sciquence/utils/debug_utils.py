from selection_utils import get_if_exist



def print_shapes(*arrays, **kwargs):
    ''
    Print shapes of all the arrays 
    
    ''
    # Parsing kwargs
    
    
    
    for arr in arrays:
        print arr.shape,
