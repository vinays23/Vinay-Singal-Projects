# The goal of this project is to create my own binary tree structure where each node in the tree is less than or equal to the child nodes. 

# In other words, I am creating a method that a user can utilize to establish a minheap.

# To accomplish this goal in Python there must be functions within a class that we can use to create our minheap. 

class BinHeap:

# First I am initializing the class and creating a heap structure that we will work with throughout this class.

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

# The next step is to create a function which moves a node up the tree structure if it is smaller than its current parent's value.        
        
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
        
# Using this function we are allowing the user to add new elements to the heap.        
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





            
