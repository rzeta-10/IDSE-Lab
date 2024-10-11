#CS22B1093 ROHAN G

class shape:
    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b
    def get_data(self,a,b):
        self.a = a
        self.b = b
    
    def display_area(self):
        return a*b
        
class rectangle(shape):
    def __init__(self,a,b):
        shape.get_data(self,a,b)
        
    # shape.get_data(self,a,b)
    
    def display_area(self):
        return shape.display_area(self)

class triangle(shape):
    def __init__(self,a,b):
        shape.get_data(self,a,b)
    # shape.get_data(self,a,b)
    def display_area(self):
        return 0.5*shape.display_area(self)

class circle(shape):
    def __init__(self,a,b):
        shape.get_data(self,a,b)
    # shape.get_data(self,a,b)
    def display_area(self):
        return 3.14*shape.display_area(self)

while True:
    print(f"1.Area of Rectangle")
    print(f"2.Area of Triangle")
    print(f"3.Area of Circle")
    print(f"4.Exit")
    choice = int(input("Choose one of the choices : "))
    if(choice == 1):
        a = float(input("Enter the length of the rectangle : "))
        b = float(input("Enter the breadth of the rectangle : "))
        if(a < 0 or b < 0):
            print(f"Entered values are negative !!")
            break
        rec = rectangle(a,b)
        print(f"The area of rectangle is {round(rec.display_area(),3)}")
    
    elif(choice == 2):
        a = float(input("Enter the height of the triangle : "))
        b = float(input("Enter the base of the triangle : "))
        if(a < 0 or b < 0):
            print(f"Entered values are negative !!")
            break
        tri = triangle(a,b)
        print(f"The are of triangle is {round(tri.display_area(),3)}")
        
    elif(choice == 3):
        a = float(input("Enter the radius of the circle : "))
        b = a
        if(a < 0 or b < 0):
            print(f"Entered values are negative !!")
            break
        cir = circle(a,b)
        print(f"The area of the cirle is {round(cir.display_area(),3)}")
        
    elif(choice == 4):
        print(f"Exiting the program .....")
        break
    
    else:
        print(f"Invalid Input. Try Again !")