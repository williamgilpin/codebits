def print_status(iter_val, final_val, max_val=79):
    '''
    Print a progress bar in a loop calculation
    
    Parameters
    ----------
    
    iter_val : int
        The current value of the iteration variable
    
    final_val : int
        The maximum value that the iteration variable 
        will eventually attain
    
    max_val : int
        The maximum width of a line. Defaults to PEP recommendation of 79
    
    
    Note: This only works in Python 3 because of the unique properties of 
            the print() function.
    '''
 
    iter_val_scaled = int((iter_val/final_val)*max_val)
    remainder = max_val-int(((final_val-1)/final_val)*max_val)
    
    print('', end="\r")
    print('[', end="")
    for jj in range(iter_val_scaled+remainder):
        print ('#', end="")
    for jj in range(max_val-iter_val_scaled-remainder):     
        print (' ', end="")
    print(']',end="")
