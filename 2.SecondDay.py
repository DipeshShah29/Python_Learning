class Car:

    wheels = 4  # Class variable

    def __init__(self):

        # Instance Variables
        self.engine = 8
        self.doors = 4
        self.brand = "BMW"

c1 = Car()
c2 = Car()

print(c1.engine, c1.doors, c1.brand, c1.wheels)

c2.engine = 9
c2.doors = 5
c2.brand = "Land Rover"
Car.wheels=6

print(c2.engine, c2.doors, c2.brand, c2.wheels)
