class Car():

    def __init__(self, colour, brand, cartype):
        self.colour= colour
        self.brand=brand
        self.type=self.CarType(cartype)

    def show(self):
        print("The car's brand is {0} and colour is {1}". format(self.brand, self.colour))

    class CarType():

        def __init__(self, type):
            self.type=type

        def show(self):
            print("The car's type is", self.type)
    

c1=Car('Red', 'Audi', 'SUV')
c1.show()

#Calling inner class
c1.type.show()
    