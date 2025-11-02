# Абстракция: общий контракт через ABC
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Площадь фигуры"""
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h
    def area(self) -> float:
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        return pi * self.r * self.r


def print_area(shape: Shape) -> None:
    # Работает с любой реализацией Shape по общему контракту
    print(f"{type(shape).__name__}: area={shape.area():.2f}")


if __name__ == "__main__":
    print_area(Rectangle(3, 4))
    print_area(Circle(2))

