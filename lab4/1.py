#CS22B1093 ROHAN G

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
p1 = Person('Alice',20)
p2 = Person('Bob',25)

p1.greet()
p2.greet()