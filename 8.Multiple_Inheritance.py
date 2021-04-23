class A:
    def func1(self):
        print("This is A's Function1")

    def func2(self):
        print("This is A's Function2")


class B:
    def func3(self):
        print("This is B's Function3")


# Class C inheriting all properties of Class A and B
class C(A, B):
    def func4(self):
        print("This is C's Function4")


a1 = A()
a1.func1()
a1.func2()
print("-------------------------------------------")
b1 = B()
b1.func3()
print("-------------------------------------------")
c1 = C()
c1.func1()
c1.func2()
c1.func3()
c1.func4()