## hw 3 part 1

def findLargest(alist):
    if len(alist) <= 1:
        return(alist[0])
   
    largest_val = findLargest(alist[1:])

    if alist[0] > largest_val:
        largest_val = alist[0]
    return largest_val    
    


