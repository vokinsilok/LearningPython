# Композиция: собираем поведение из частей и делегируем

class Engine:
    def start(self) -> None:
        print("Двигатель запущен")


class GPS:
    def locate(self) -> tuple[float, float]:
        # Заглушка
        return (55.75, 37.62)


class Car:
    def __init__(self, engine: Engine, gps: GPS | None = None):
        self.engine = engine
        self.gps = gps

    def drive(self) -> None:
        # Делегирование действия компонентам
        self.engine.start()
        if self.gps:
            print("Текущие координаты:", self.gps.locate())


if __name__ == "__main__":
    car1 = Car(Engine())
    car1.drive()

    print("---")
    car2 = Car(Engine(), GPS())
    car2.drive()

