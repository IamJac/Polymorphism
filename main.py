from math import pow,pi
from Abstract_class_module import Shape
class Rectangle(Shape):
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return pi*pow(self.radius,2)
class Sphere(Shape):
    def __init__(self,r1):
        self.radius1=r1
    def area(self):
        return 4*pi*pow(self.radius1,2)
print("Input details of the rectangle")
num1=int(input("Input length"))
num2=int(input("Input width"))
rec=Rectangle(num1,num2)
print("Input details of the circle")
num3=int(input("Input radius"))
circ=Circle(num3)
print("Input details of the Sphere")
num4=int(input("Input radius"))
sph=Sphere(num4)
print("Area of the rectangle is ",rec.area(),"cm^2")
print("Area of the circle is ",circ.area(),"cm^2")
print("Area of the Sphere is ",sph.area(),"cm^2")
