##Number 1

def frisbeeSort(alist):
   length = len(alist) 
  
   while length > 0:
       index = 0
       
       max_elem = max(alist[:length])
       index = alist.index(max_elem)

       alist[:index+1] = reversed(alist[:index+1])
       alist[:length] = reversed(alist[:length])
       length -= 1 






##Number 2
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp



    for a in range(len(alist)):
        for x in range(0, len(alist)-a-1):
            if alist[x] > alist[x+1]:
                swap = alist[x]
                alist[x] = alist[x+1]
                alist[x+1] = swap





##Number 3
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        a = 0
        lefthalf = []
        righthalf = []

        for a in range(mid):
            lefthalf.append(alist[a])

        for a in range(mid, len(alist)):
            righthalf.append(alist[a])
            

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)






            
