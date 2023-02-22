# Requirement: Build a minheap wihout using Python delivered functions; using a customizied binary tree structure where each node in the tree is less than or equal to the child nodes.
# Solution: Create a customized binary tree structure.  

# HOW I CONSTRUCTED THE SOLUTION:

class BinHeap:

# STEP 1: Function 1 - Initialize the class and create a heap structure to use throughout this method.

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

# STEP 2: Function 2 - Moves a node up the tree structure if it is smaller than its current parent's value.        
        
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
        
# STEP 3: Function 3 - Enables the user to add new elements to the heap.  

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
# STEP 4: Function 4 - Moves a node down the tree structure if it is greater than its children's value.         

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
# STEP 5: Function 5 - Returns the location of the smallest child at position i.

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
# STEP 6: Function 6 - Removes and subsequently returns the smallest value in the heap.

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
# STEP 7: Function 7 - Creates a heap from a given list of values.
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

# STEP 8: Function 8 - Using previously defined functions, this sorts the heap.             
            
    def heapSort(self):
        alist = []

        for i in self.heapList[1:]:
            alist.append(self.delMin())
        self.buildHeap(alist)

# STEP 9 (FINAL STEP): Function 9 - Prints the sorted heap        
        
    def printList(self):
        print(self.heapList[1:])







            
