# Наследование: базовый и производные классы

class Animal:
    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


class ServiceDog(Dog):
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        # расширяем поведение Dog
        return f"{self.name}: woof"


if __name__ == "__main__":
    animals = [Animal(), Dog(), Cat(), ServiceDog("Rex")]
    for a in animals:
        print(type(a).__name__, "->", a.speak())

