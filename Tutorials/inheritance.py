class Animal:
    def action(self,action):
        # self.action = action
        pass
        

class Dog(Animal):
    def action(self):
        print(f'Dog {action}ed')
    

class Cat(Animal):
    def action(self):
        print(f'Cat {action}ed')
    

    
action = input("what should an animal do?: ")

object_dog = Dog()
object_cat = Cat()


# object_dog.action()
object_cat.action()
