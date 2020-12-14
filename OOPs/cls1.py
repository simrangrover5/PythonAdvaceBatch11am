
from time import sleep

class Animal:
    __slots__ = ['type','color','age']  #in this we have defined the attributes which we can make for our object
    def __init__(self,type1,color):
        self.type =  type1
        self.color = color
    
    def __str__(self):  #std output
        return f"Type : {self.type}"
    
    def __repr__(self):  #shell output
        return f"{self.type}"
    
    def show_attr(self):
        print("\n Type : ",self.type)
        print("\n Color : ",self.color)
        
    def __del__(self):
        print("\n Deleting Type....")
        del self.type
        sleep(2)
        print("\n Deleting Color.....")
        del self.color
        sleep(2)
        print("\n Deleting Self.....")
        del self
        sleep(2)
        
a1 = Animal("Cow", "White")
a2 = Animal("Cat", "Black")

print("Object 1 : ", a1)
print("\n Object 2 : ", a2)

a1.age = 3
a2.age = 2

print("\n Deleting Age Attribute")
del a1.age  #when you delete particular attribute then default del is called

del a1 #__del__
del a2 #__del__

print(a1)
