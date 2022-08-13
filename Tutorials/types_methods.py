
class Student():

    school = 'MMCOE'

    def __init__(self):
        self.m1 = 12
        self.m2 = 24

    def get(self):          ## instance Method
        return self.m1
    
    @classmethod            ## Decorators 
    def info(cls):          ## Class method
        return cls.school

    @staticmethod
    def get_classname():
        print('This is Class in abc')

obj = Student()
print(obj.get())
print(Student.info())
Student.get_classname()