# Полиморфизм (duck typing): работаем по поведению, а не по типу

class Circle:
    def __init__(self, r: float):
        self.r = r
    def draw(self) -> None:
        print(f"Рисую круг радиуса {self.r}")

class Square:
    def __init__(self, a: float):
        self.a = a
    def draw(self) -> None:
        print(f"Рисую квадрат со стороной {self.a}")

# Функция не знает конкретные классы, ей важно только, чтобы у объекта был метод draw()
def render(obj) -> None:
    obj.draw()

if __name__ == "__main__":
    objects = [Circle(2), Square(3), Circle(1.5)]
    for obj in objects:
        render(obj)

