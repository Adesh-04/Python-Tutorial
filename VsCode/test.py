
## [[data][ptr]] -> [[data][ptr]] -> None

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LL():
    def __init__(self):
        self.head = None

    def add(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.add(self.head.next,data)
    
    def display(self):
        if self.head:
            print(self.head.data)
            if self.head.next:
                self.head.next.display()


obj = LL()
obj.add(20)
obj.add(30)
obj.display()