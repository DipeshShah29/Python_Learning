# Public variable => variableName       accessible to class, derived class an anywhere outside the derived class
# Protected Variable => _variableName   accesible to class and its derived class
# Private Variable => __variableName    accessibe to class only

class car():
    color = 'Black'
    _modelName='BMW'
    __yearofManufacture=2017
    print("Private Variable is __yearofManufacture", __yearofManufacture)

    def show(self):
        #self._modelName='Audi'
        #self.color='Red'
        print("Public variable color is {0} and Protected Variable _modelName is {1}".format(self.color, self._modelName))

        # Private variable is not accessible outside the class but it can be made accessible like this: (not advisable)
        print("and Private Variable __yearofManufacture is", self._car__yearofManufacture)  

class truck():
    print("The color of the truck is", color)


car1=car()
car1._modelName='Mercedes'
car1.color='Blue'
car1._car__yearofManufacture=2018       # Wrong practice though
car1.show()

truck1=truck()
