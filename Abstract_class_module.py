import abc
from abc import ABC
class Shape(ABC):
    @abc.abstractmethod
    def area(self):#Method to be overridden
        print("Area of shape")
