import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

r = float(input("Enter radius: "))
c = Circle(r)
print("Area:", c.area())
print("Diameter:", c.diameter())

