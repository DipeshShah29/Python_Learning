class A:
    def __init__(self):
        print("You are in A's init function")

    def func1(self):
        print("This is A's func1")


class B(A):
    def __init__(self):
        super().__init__()
        print("You are in B's init function")

    def func2(self):
        print("This is B's func2")


a1 = B()
