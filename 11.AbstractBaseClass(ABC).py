# Why use Abstract Base Classes:
# An abstract method is a method that has a declaration but does not have an implementation.
# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.
# This capability is especially useful in situations where a third-party is going to provide implementations,
# such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all classes
# in your mind is difficult or not possible.

from abc import ABC, abstractmethod


class animal(ABC):

    # A method becomes abstract when decorated with the keyword @abstractmethod.
    # Once a method has been declared as an Abstract method, it can't be instantiated. 
    # You can instantiate otherwise and it still will work
    @abstractmethod
    def behavior(self):
        pass

    def avgLife(self):
        pass


class dog(animal):
    def behavior(self):
        print("I can bark")

    def avgLife(self):
        print("My avg life is 8 yrs")


class snake(animal):
    def behavior(self):
        print("I can crawl")

    def avgLife(self):
        print("My avg life is 20 yrs")


#a = animal()       #This will work only without @abstractmethod decorator
d = dog()
d.behavior()
d.avgLife()

s = snake()
s.behavior()
s.avgLife()