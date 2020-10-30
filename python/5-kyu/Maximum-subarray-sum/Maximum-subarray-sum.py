def max_sequence(arr):
	
    Current = Max = 0

    for x in arr:
        
        Current += x
        if Current < 0: Current = 0
        if Current > Max: Max = Current
            
    return Max
