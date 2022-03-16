class person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi, How are you? {self.name} ')


name=input("Enter your name: ")
object = person(name)
object.talk()


