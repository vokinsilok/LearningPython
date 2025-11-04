class Temperature:
    def __init__(self, acelsius: float=0.0):
        self.__celsius = acelsius

    @property
    def celsius(self) -> float:
        return self.__celsius

    @celsius.setter
    def celsius(self, value) -> None:
        if value < -273.15:
            raise ValueError("celsius cannot be negative")
        self.__celsius = value

    @property
    def fahrenheit(self) -> float:
        return self.__celsius * 1.8 + 32




a = Temperature(5)
print(a.celsius)
a.celsius = -273
print(a.celsius)
print(a.fahrenheit)

