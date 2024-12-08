def mo(*args):
    result = 1
    for num in args:
        if isinstance(num, int):
            result = result * num

    return result

def new_mo(**kwargs):
    result = 1
    for key in kwargs:
        result = result * kwargs[key]
    return result


result = mo(2,3,4,5)
print(
    'the result is: {}'.format(result)
)

result = mo(1,2,3,4,5,6,7)
print(
    'the result is: {}'.format(result)
)

result = new_mo(num1=20,num2=20)
print(
    'the result is: {}'.format(result)
)

items={'num1':20,'num2':20, 'num3':30}
result = new_mo(**items)
print(
    'the result is: {}'.format(result)
)