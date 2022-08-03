
class Stack():
    def __init__(self,size):
        self.stack = []
        self.size = size
    
    def push(self,data):
        if data not in self.stack and len(self.stack)!=self.size:
            self.stack.append(data)

    def pop(self):
        return self.stack.pop() if len(self.stack)!=0 else 'no item to pop'
    
    def top(self):
        return self.stack[-1] if len(self.stack)!=0 else 'no item at top'

    def isEmpty(self):
        return False  if len(self.stack)>0 else True  

    def isFull(self):
        return True if len(self.stack) >= self.size else None

## Testing

# stack = Stack(5)
# stack.push(10)
# stack.push(20)
# # stack.push(30)
# # stack.push(40)
# # stack.push(50)
# # stack.push(60)
# # stack.push(70)
# # stack.push(80)
# # print(stack.top())
# # stack.pop()
# # stack.push(22)
# print(stack.top())
# stack.isEmpty()
# stack.isFull()


## reverse string using stack without duplicates

string = 'abcd123ny'
reverse = ''
new_list = []

for x in string:
    new_list.append(x)

rev = Stack(len(new_list))

for x in new_list:
    rev.push(x)

# rev.isEmpty()

while rev.isEmpty() == False:
    val = rev.top()
    rev.pop()
    reverse += val

print(f'reverse of {string} is {reverse}')


