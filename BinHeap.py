# Requirement: Build a minheap wihout using Python delivered functions; using a customizied binary tree structure where each node in the tree is less than or equal to the child nodes.
# Solution: Create a customized binary tree structure.  

# HOW DID I CONSTRUCT THE SOLUTION:

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

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def heapSort(self):
        alist = []

        for i in self.heapList[1:]:
            alist.append(self.delMin())
        self.buildHeap(alist)

    def printList(self):
        print(self.heapList[1:])


#a = [1, 2, 5, 3, 6, 9, 8, 25, 20]

bh = BinHeap()


bh.insert(5)
bh.insert(8)
bh.insert(6)
bh.insert(2)
bh.insert(12)
bh.insert(11)

bh.heapSort()
bh.printList()





            
