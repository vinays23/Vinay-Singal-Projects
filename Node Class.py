#GOAL: Modify and manipulate a node within a linked list without using Python's built-in functions.

class Node:
    
    #Function 1: Initialize the class.
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    #Function 2: Return the value of the node.
    
    def getData(self):
        return self.data

    #Function 3: Return the value of the next attribute of the current node.
    
    def getNext(self):
        return self.next

    #Function 4: Set the value of a node to a new value.
    
    def setData(self,newdata):
        self.data = newdata

    #Function 5: Set the value of the next node to a new value.
    
    def setNext(self,newnext):
        self.next = newnext

        
#Function 6: Traverses through the linked list to see if there is a specific node value within the list.        
        
def findValue(val, node):

    #If value matches node, return true.
    
    if node.getData() == val:
        return True


    if node.getNext() == None:
        return False

    found_val = findValue(val, node.getNext())

    return found_val

#if value does not match node, delegate the task to the next node.

    if node.getNext() != None:
        
        found_val = findValue(val, node.getNext())

    if node.getNext() == None:
        if node.getData() != val:

            return False
    
    return found_val

    
