# inheritance using 
class Person:
    def __init__(self,first,last,age):
        self.firstname = first
        self.lastname = last
        self.age = age

# must be included to 'print(x)'    
    def __str__(self):
        return self.firstname + " " + self.lastname + "," + str(self.age)

class Employee(Person):
    def __init__(self,first,last,age,staffnum):
        super().__init__(first, last, age)               # use of 'super' keyword 
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + "," + self.staffnumber

x = Person("Barney", "Stinson", "19")
y = Employee("Mark", "Mueller", "20", "1000")
print(x)
print(y)                        
