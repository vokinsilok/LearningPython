class Rectangle:
    def __init__(self, w: float, h: float):
        if w <= 0 or h <= 0:
            raise ValueError("w и h должны быть > 0")
        self.w = float(w)
        self.h = float(h)

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)

    def __repr__(self) -> str:
        return f"Rectangle(w={self.w:g}, h={self.h:g})"
