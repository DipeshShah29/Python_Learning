class first:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2


sum1 = first()
print(sum1.add(5, 10))

sum2 = first()
print(sum2.add(45, 999))


class Second:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def Multiply(self):
        return self.number1 * self.number2


mul1 = Second(123, 34.35)
result = mul1.Multiply()
print("Multiplication result: ", format(result))
