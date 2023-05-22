from abc import ABC
from math import pi


class Figure(ABC):
    def __init__(self):
        self.__perimetr = None
        self.__square = None

    def get_perimeter(self):
        pass

    def get_square(self):
        pass


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if a + b > c and a + c > b and b + c > a:
            super().__init__()
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise ValueError("Такого трикутника не існує")


    def get_perimeter(self):
        self.__perimetr = self.__a + self.__b + self.__c
        return self.__perimetr

    def get_square(self):
        p = self.get_perimeter() / 2
        self.__square = (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5
        return self.__square


class Circle(Figure):
    def __init__(self, r: float):
        super().__init__()
        self.r = r

    def get_perimeter(self):
        self.__perimetr =  2 * pi * self.r
        return self.__perimetr

    def get_square(self):
        self.__square =  pi * self.r ** 2
        return self.__square



class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        super().__init__()
        self.a = a
        self.b = b

    def get_perimeter(self):
        self.__perimetr =  2 * (self.a + self.b)
        return self.__perimetr

    def get_square(self):
        self.__square =  self.a * self.b
        return self.__square



class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

