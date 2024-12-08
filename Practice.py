class get_func_name():
    def __init__(self, num1, num2):
        self.fisrtNumber = num1
        self.secondNumber = num2
        self.result = 0

    def add(self):
        self.result = self.fisrtNumber + self.secondNumber
        return self.result

    def sub(self):
        self.result = self.fisrtNumber - self.secondNumber
        return self.result

func_name = get_func_name(1,2)
add_result  = func_name.add()
print('The result of addition is: {0}'.format(add_result))

add_1_result = func_name.add(2,3,5)
print('the result of the addition of 3 numbers is: {0}'.format(add_1_result))

sub_result = func_name.sub()
print('the result of subtraction is: {0}'.format(sub_result))
