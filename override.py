# Method Overriding
class Shapes:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area Of Rectangle : " ,self.length * self.breadth)

class Rectangle(Shapes):
    def __init__(self, length, breadth):
        super().__init__(length,breadth)
        self.breadth = breadth

    def area(self):
        super().area()
        return "Area Of Rectangle : " ,self.length * self.breadth

length = float(input("Enter Length : "))  
breadth = float(input("Enter Breadth : "))     

a2 = Rectangle(length, breadth)
print(a2.area())                  