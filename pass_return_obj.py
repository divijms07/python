# Passing and returning an obj to/from  user defined functions
class TwoNum:
    def GetNum(self):
        self.__x = int(input("Enter value of x : "))
        self.__y = int(input("Enter value of y : "))

    def PutNum(self):
        print("Value of x = ",self.__x,"Value of y = ",self.__y)    

    def Add(self,T):
        R = TwoNum()
        R.__x = self.__x + T.__x  
        R.__y = self.__y + T.__y  
        return R                          # returning an obj from function


obj1 = TwoNum()
obj2 = TwoNum()
print("Values of x and y for object 1 : ")
obj1.GetNum()  
print("Values of x and y for object 2 : ")
obj2.GetNum()    

obj3 = obj1.Add(obj2)                    # Passing an object to function as an argument
print("Object 1")
obj1.PutNum()
print("Object 2")
obj2.PutNum()
print("Sum of two objects - Object 3")
obj3.PutNum()


