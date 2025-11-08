class Area:
    #def __init__(self) -> None:

    @staticmethod
    def circle(r: float):
        return Area.checer(3.14 * r ** 2)

    @staticmethod
    def rectangle(a: float, b: float):
        return Area.checer(a * b)

    @staticmethod
    def square(a: float):
        return Area.checer(a * a)

    @staticmethod
    def triangle(a: float, h: float):
        return Area.checer((a * h) / 2)

    @staticmethod
    def checer(self):
        if not isinstance(self, float):
            raise ValueError(f"value must be float or int and not {self}")
        elif self <= 0:
            raise ValueError("value must be positive")
        else:
            return self

    def __repr__(self):
        raise SyntaxError("'Area' must have any method")


print(Area.circle(3.0))
print(Area.rectangle(3.0, 4.0))
print(Area.square(3.5))
print(Area().square(3.0))
print(Area.triangle(3.0, 4.0))
print(Area().circle)
#print(Area())
