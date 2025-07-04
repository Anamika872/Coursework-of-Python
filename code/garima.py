class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def area(self):
        pi = 3.1416
        return pi * (self.radius ** 2)      

c1 = Circle(4)
c2 = Circle(10)

print(c1.area()) 
print(c2.area())
