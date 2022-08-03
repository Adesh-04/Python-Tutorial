
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue)>0:
            return(self.queue.pop(0))

    def displayQ(self):
        listQ = []
        for x in self.queue:
            listQ.append(x)
        print(listQ)
        return(listQ)
    
    def isEmpty(self):
        return True if len(self.queue) == 0 else False
        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(4)
# print(queue.isEmpty())
queue.displayQ()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.displayQ()
# print(queue.isEmpty())
    