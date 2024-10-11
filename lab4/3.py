#CS22B1093 ROHAN G

class Animal:
    # def __init__(self):
    def make_sound(self):
        print(f"Some Sound")
    
class Dog(Animal):
    def make_sound(self):
        print(f"Woof")
    
class Cat(Animal):
    def make_sound(self):
        print(f"Meow")
        
dog = Dog().make_sound()
cat = Cat().make_sound()