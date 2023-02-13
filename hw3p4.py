def ternarySearchRec(alist, item):
    if alist == []:
        return False
    else:
        midpoint1 = len(alist)//3
        midpoint2 = 2*(midpoint1)

        if alist[midpoint1] == item or alist[midpoint2] == item:
            return True
        elif item < alist[midpoint1]:

            return ternarySearchRec(alist[:midpoint1], item)
        elif item > alist[midpoint2]:

            return ternarySearchRec(alist[midpoint2 + 1:], item)
        else:
            return ternarySearchRec(alist[midpoint1 + 1 : midpoint2], item)
            

