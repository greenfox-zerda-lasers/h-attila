# Create a class called "Car"
# It should have a "type" property that stores the car's type in a string eg: "Mazda"
# It should have a "km" property that stores how many kilometers it have run
# The km and the type property should be a parmeter in the constructor
# It should have a method called "run" that takes a number and increments the "km" property by it


class Car():

    type = ""
    km = 0

    def __init__(self, type, km):

        self.type = type
        self.km = km

    def ride(self, runned_km):
        self.runned_km = runned_km
        self.km += self.runned_km
        return self.km


my_mazda = Car("mazda", 12000)
my_mazda.ride(100)
print(my_mazda.type)  # "mazda"
print(my_mazda.km)  # 12100
