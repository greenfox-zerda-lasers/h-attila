# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

import math


class Circle():

    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return self.radius ** 2 * math.pi


mycircle = Circle(4)
print(mycircle.get_circumference())
print(mycircle.get_area())
