# Simple Inheritance
class User:
    def __init__(self,name):
        self.name = name

    def printName(self):
        print("Name : " + self.name)

class Programmer(User):
    def __init__(self, name):
        self.name = name   

    def LearnPython(self):
        print("Learning Python Language")   

u1 = User("Brian")
u1.printName()
p1 = Programmer("John")
p1.LearnPython()                      