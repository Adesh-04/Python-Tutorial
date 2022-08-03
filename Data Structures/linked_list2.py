
from dataclasses import dataclass


class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.nextNode = next

class LinkedList (object):
    def __init__(self,root = None):
        self.root = root
        self.size = 0

    def add (self,data):
        new_node = Node(data,self.root)
        self.root = new_node
        self.size += 1
    def find(self,data):
        this_node = self.root
        while this_node:
            if this_node.data == data:
                return 'found'
            else:
                this_node = this_node.nextNode
        return None
    def get_list(self):
        this_node = self.root
        while this_node:
            print(this_node.data,end=' ')
            this_node = this_node.nextNode

myList = LinkedList()
myList.add(10)
myList.add(20)
print(myList.find(10))
print(myList.find(100))
myList.get_list()
