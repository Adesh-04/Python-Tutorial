
from tempfile import tempdir


class Node():
    def __init__(self,prev = None, data = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev


class DLL():
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def addBegin(self,data):
        newNode = Node(None,data,self.head)
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def addMiddle(self,index,data):
        prevNode = None
        tmpNode = self.head
        nextNode = None
        if index == 0:
            self.addBegin(data)
        if index >= self.size:
            self.addEnd(data)
        elif index > 0 and index < self.size:
            for i in range(0,index):
                tmpNode = tmpNode.next
                print(i)
            prevNode = tmpNode.prev
            newNode = Node(prevNode,data,tmpNode)
            prevNode.next = newNode
            newNode.prev = prevNode 
            self.size+=1           
       
    def addEnd(self,data):
        newNode = Node(None,data,None)
        
        if self.head == None:
            newNode.prev = None
            self.head = newNode
        
        firstNode = self.head
        while firstNode.next:
            firstNode = firstNode.next
        
        firstNode.next = newNode
        newNode.prev = firstNode
        self.size +=1

    def display(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.data,end=' ')
            tempNode = tempNode.next

    def remove(self,data):
        tempNode = self.head
        prevNode = None
        nextNode = self.head.next
        while tempNode:
            if tempNode.data == data:
                if prevNode:
                    prevNode.next = tempNode.next
                    nextNode.prev = tempNode.prev
                else:
                    self.head = tempNode.next
                self.size -= 1
                return True
            else:
                prevNode = tempNode
                tempNode = tempNode.next
                nextNode = tempNode.next
        return False

    def removeIndex(self,index = None):  ## Need TO  Complete
        if index == 0:
            self.remove(self.head.data)

        elif index > 0 and index < self.size:
            tmpNode = self.head
            for i in range(0,index):
                tmpNode = tmpNode.next
            self.remove(tmpNode.data)        


LL = DLL()
LL.addBegin(12)
LL.addBegin(13)
LL.addBegin(14)
LL.addBegin(15)
LL.addBegin(16)
# LL.addMiddle(6,100)
# LL.remove(13)
LL.removeIndex(3)
LL.display()
