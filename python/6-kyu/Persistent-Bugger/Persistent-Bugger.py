import numpy 
def persistence(n):
    
    toList = list(str(n))
       
    SplittedNums = numpy.array(toList).astype(numpy.integer)
    
    Length = len(SplittedNums)
    
    Count = 0
    
    while Length > 1:
        Product = list(str(numpy.prod(SplittedNums)))
        SplittedNums = numpy.array(Product).astype(numpy.integer)
        Length = len(Product)
        Count += 1
        
    return Count
        
