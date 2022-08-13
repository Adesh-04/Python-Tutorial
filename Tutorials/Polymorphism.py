# a=3
# b=4
# c=5
# print(a + b)  # --> int.__add__(a,b)
# print(c)      # --> int.__str__()

class Student():
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        a= self.a + other.a
        return a
    def __str__(self):
        return '{}'.format(self.a)

obj1 = Student(5)
obj2 = Student(10)

print(obj1,'print')
print(obj2,'print')

obj3 = obj1 + obj2  # --> class i.e Students.__add__(obj1,obj2)
print(obj3)


class pygame():
    def execute(self):
        print('compile')
        print('run')

class Type():
    def code(self,key):
        key.execute()

key = pygame()

obj = Type()
# obj.code(key)