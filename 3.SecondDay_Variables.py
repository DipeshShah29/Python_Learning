class Car:

    wheels = 4  # Class variable

    def __init__(self):

        # Instance Variables
        self.engine = 8
        self.doors = 4
        self.brand = "BMW"

    # Instance Method: Works with Instance Variables
    def GetBrandName(self):
        return self.brand

    @classmethod  # Works with class variables
    def GetWheelsInfo(cls):
        return cls.wheels

    @staticmethod  # Works with static variables
    def GetInfo():
        value='Static'
        print("This is {0} Method".format(value))

# Calling the Methods

# 1. Calling Instance Method
c1 = Car()
print(c1.engine, c1.doors, c1.brand, c1.wheels)

# 2. Calling Class Method
print(Car.GetWheelsInfo())

# 3. Calling Static Method
Car.GetInfo()
