
class Node():
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def add(self,data):
        new_node = Node(data,self.head)
        self.head = new_node
        self.size += 1

    def remove(self,data):
        temp_node = self.head
        prev_node = None
        while temp_node:
            if temp_node.data == data:
                if prev_node:
                    prev_node.next = temp_node.next
                else:
                    self.head = temp_node.next
                self.size -= 1
                return True
            else:
                prev_node = temp_node
                temp_node = temp_node.next
        return False


    def display(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next


List = LinkedList()
List.display()
List.add(10)
List.add(20)
List.add(30)
List.remove(30)
List.add(123)
List.add(0)
List.display()