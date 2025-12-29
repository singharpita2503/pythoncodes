#OBJECT ORIENTED PROGRAMMING
class Student:
    name="Asmita"
    roll=100

s1=Student()
print(s1.name)
print(s1.roll)
    
class Student:
    def __init__(self,name,roll):
        print(name)
        print(roll)
s1=Student("Riya",23)    

class Student:
    def __init__(self):
        print("not parameterized")
    def info(self):
        print("Shreya")
        print("21")
s1=Student()
s1.info()

"""class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print(area)
class Square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print(area)
obj=Square()
obj.rec_area(10,40)
obj.squ_area(10)"""                

class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of rectangle: ",area)
class Square:
    def squ_area(self,side):
        area=side*side
        print("Area of square: ",area)
class Triangle(Rectangle,Square):
    def tri_area(side,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle: ",area)
obj=Triangle()
obj.rec_area(10,40)
obj.squ_area(10) 
obj.tri_area(12,13) 

class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of rectangle: ",area)
class Square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of square: ",area)
class Triangle(Square):
    def tri_area(side,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle: ",area)
obj=Triangle()
obj.rec_area(10,40)
obj.squ_area(10) 
obj.tri_area(12,13)  

class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of rectangle: ",area)
class Square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of square: ",area)
class Triangle(Square):
    def tri_area(side,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle: ",area)
obj=Triangle()
obj.rec_area(10,40)
obj.squ_area(10) 
obj.tri_area(12,13)  

class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of rectangle: ",area)
class Square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of square: ",area)
class Triangle(Rectangle):
    def tri_area(side,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle: ",area)
squ=Square()
tri=Triangle()

squ.rec_area(2,3)
squ.squ_area(2)
tri.tri_area(4,5)

class Public:
    def __init__(self):
        self.name="Riya"

    def display_name(self):
        print(self.name)

obj=Public()
obj.display_name()
print(obj.name) 

class Private:
    def __init__(self):
        self.name="Riya"

    def display_name(self):
        print(self.name)

obj=Private()
obj.display_name()
print(obj.name)             

class Protected:
    def __init__(self):
        self.name="Riya"

    def display_name(self):
        print(self.name)

obj=Protected()
obj.display_name()
print(obj.name) 