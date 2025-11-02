# ООП в Python

Зачем это нужно
- Делить код на понятные сущности (классы) и управлять сложностью.
- Скрывать детали реализации и предоставлять простой интерфейс.
- Переиспользовать и расширять поведение без дублирования.

Ключевые идеи (5 штук)

1) Инкапсуляция — скрываем «как», оставляем «что»
- Идея: публичный интерфейс стабилен, реализацию можно менять.
- В Python «приватность» — договорённость: name (публично), _name (внутренне), __name (name mangling: _Class__name).
- Инструменты: свойства (@property), дескрипторы, модули, иммутабельность.
Пример:
```python
class Account:
    def __init__(self, balance: float = 0.0):
        self._balance = float(balance)
    @property
    def balance(self) -> float:  # чтение как поле
        return self._balance
    def deposit(self, amount: float) -> None:
        if amount <= 0: raise ValueError
        self._balance += amount
```

2) Наследование — «X является Y» (is‑a)
- Подкласс — частный случай базового, обязан соблюдать его контракт (LSP).
- Подходит, когда нужно расширить поведение, не ломая инварианты базы.
Пример:
```python
class Animal:
    def speak(self) -> str: return "..."
class Dog(Animal):
    def speak(self) -> str: return "woof"
```
Замечания: используйте super() при переопределении, избегайте глубоких иерархий.

3) Полиморфизм — работаем по поведению, а не по типу
- Функция принимает «то, что умеет нужный метод», конкретный класс не важен.
Пример (duck typing):
```python
def draw(obj):
    obj.draw()  # любой объект с методом draw()
```
С typing.Protocol (для статпроверки):
```python
from typing import Protocol
class Drawable(Protocol):
    def draw(self) -> None: ...
```

4) Абстракция — оставляем главное, прячем лишнее
- Объявляем «что должно быть», не показывая «как внутри».
Пример (ABC):
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
```

5) Композиция — «собираем из частей» (has‑a)
- Класс хранит другие объекты и делегирует им работу. Гибче наследования.
Пример:
```python
class Engine: 
    def start(self): print('engine start')
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
    def drive(self):
        self.engine.start()  # делегирование
```
Правило: по умолчанию предпочитайте композицию, а не наследование.

Мини‑инструменты, которые пригодятся
- Свойства (@property): инкапсуляция и валидация без смены API.
- Dataclass: быстрые модельные классы.
```python
from dataclasses import dataclass
@dataclass
class User: id: int; name: str
```
- Магические методы: __repr__ (удобный вывод), __len__/__iter__ (итерируемость), __enter__/__exit__ (контекстный менеджер).
```python
class Timer:
    from time import perf_counter
    def __enter__(self):
        from time import perf_counter; self.t0 = perf_counter(); return self
    def __exit__(self, *a):
        from time import perf_counter; self.dt = perf_counter() - self.t0
```

Короткий чек‑лист выбора
- Нужно «особый случай» того же контракта? — наследование (и только если LSP не ломается).
- Нужно собрать поведение из разных ролей? — композиция (Strategy/Decorator/Adapter).
- Важно удержать инварианты? — свойства/дескрипторы, меньше публичного состояния.
- Хотите взаимозаменяемость реализаций? — ABC/Protocol + внедрение зависимостей.

Мини‑примеры
- Точка:
```python
class Point: 
    def __init__(self, x: float, y: float): self.x, self.y = x, y
```
- Вектор с операторами:
```python
class Vector2D:
    def __init__(self, x: float, y: float): self.x, self.y = x, y
    def __add__(self, o): return Vector2D(self.x + o.x, self.y + o.y)
    def __repr__(self): return f"Vector2D({self.x}, {self.y})"
```

Задания (кратко)
База
1) Rectangle: area(), perimeter(), __repr__
2) BankAccount: deposit/withdraw c валидацией, свойство balance
3) Vector2D: __add__/__sub__/__repr__
4) Temperature: property celsius/fahrenheit
5) Notebook: add, __len__, __iter__, __getitem__

Средние
1) Shape (ABC) + Circle/Rectangle/Triangle: area(), сравнение по площади
2) Polynomial: __call__, __add__, __mul__
3) Warehouse: add/take, исключение при нехватке

Вопросы и короткие ответы
1) Класс vs объект? — Шаблон vs экземпляр.
2) Зачем @property? — Валидация/инкапсуляция без смены API.
3) Наследование или композиция? — Обычно композиция; наследование, если «is‑a» и LSP.
4) Что такое полиморфизм? — Работа по общему поведению (протоколу).
5) Для чего ABC? — Фиксирует контракт интерфейса.
6) Чем статический метод отличается от метода класса? — Нет self/cls vs есть cls.
7) Что делает __repr__? — Удобное представление для отладки.
8) Как сделать класс итерируемым? — __iter__ или __getitem__ с индексами.
9) Когда писать свои исключения? — Для доменных ошибок.
10) Как тестировать ООП‑код? — По контрактам интерфейсов, мокая зависимости.

Стиль и привычки
- PEP 8, понятные имена, короткие методы, информативный __repr__, аннотации типов.
- Публичного — минимум, инварианты — проверять, тесты — покрывают поведение.
