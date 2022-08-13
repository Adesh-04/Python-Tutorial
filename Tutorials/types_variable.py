
class Car:
    wheel = 'qwe'       ## Class or Static Variable
    def __init__(self):
        self.A = 5     ## instance Variables


c1 = Car()
c2 = Car()

c1.A = 10               ## changed by instances of the class
Car.wheel = 'abc'       ## changed by class itself

Car.A = 11              ## Does not work becoz A is not a class variable

print(c1.A,c2.A)
print(c1.wheel,c2.wheel)