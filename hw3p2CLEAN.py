class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

def findValue(val, node):

#if value matches node, return true.
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

    
#    print(findValue(node.getNext(), val))
    

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n2.setNext(n1)
n3.setNext(n2)
n4.setNext(n3)

print(findValue(40, n2))
