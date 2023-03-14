#Inheritance Using GET Method
#super class
class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self,first,last,staffnum):
        Person.__init__(self, first, last)           # using Super Class
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + " " + self.staffnumber

x = Person("Ted", "Mosby") 
y = Employee("Anthony", "Elanga", "10") 
print(x.Name())
print(y.GetEmployee())      