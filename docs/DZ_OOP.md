# Домашнее задание: ООП в Python (понятные требования и ожидаемые результаты)

Как сдавать
- Python 3.12+
- Соблюдать PEP 8, аннотации типов. К публичным классам/методам — короткий docstring.
- Каждый класс — в отдельном файле или логически сгруппированы (папка src/ допустима).
- Добавьте простые примеры использования (doctest) или минимальные тесты (pytest) для проверки.

Критерии зачёта
- Реализовано ровно то, что описано в разделе «Реализовать».
- Поведение совпадает с «Ожидаемым результатом» (примеры проходят).
- Код читаемый, без избыточной сложности.

Часть A — База

1) Rectangle — класс прямоугольника
Что нужно сделать
- Создать класс прямоугольника, уметь считать площадь и периметр.
Реализовать
- __init__(w: float, h: float) — ширина и высота > 0 (иначе ValueError).
- area() -> float — площадь.
- perimeter() -> float — периметр.
- __repr__ -> str вида Rectangle(w=..., h=...).
Ожидаемый результат — Примеры (doctest)
```python
>>> Rectangle(3, 4).area()
12.0
>>> Rectangle(3, 4).perimeter()
14.0
>>> repr(Rectangle(2, 5))
'Rectangle(w=2, h=5)'
```

2) BankAccount — банковский счёт
Что нужно сделать
- Создать счёт с пополнением и снятием, с защитой от перерасхода.
Реализовать
- Класс ошибки OverdraftError.
- Класс BankAccount(balance: float = 0.0).
- Свойство balance (только для чтения).
- deposit(amount: float) — amount > 0, иначе ValueError.
- withdraw(amount: float) — amount > 0; если amount > balance — OverdraftError.
Ожидаемый результат — Примеры (doctest)
```python
>>> acc = BankAccount(100)
>>> acc.deposit(50); acc.balance
150.0
>>> acc.withdraw(20); acc.balance
130.0
>>> acc.withdraw(1000)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
OverdraftError: ...
```

3) Vector2D — вектор в 2D
Что нужно сделать
- Сложение/вычитание векторов, умножение на скаляр, сравнение и представление.
Реализовать
- __init__(x: float, y: float)
- __add__(other: Vector2D) -> Vector2D
- __sub__(other: Vector2D) -> Vector2D
- __mul__(k: float) -> Vector2D и __rmul__(k: float) -> Vector2D
- __eq__(other: object) -> bool, __repr__ -> str
Ожидаемый результат — Примеры (doctest)
```python
>>> 2 * Vector2D(1, 2) + Vector2D(3, 4)
Vector2D(5, 8)
>>> Vector2D(1, 1) == Vector2D(1, 1)
True
```

4) Temperature — свойства и валидация
Что нужно сделать
- Хранить температуру в °C, давать доступ к °F, не допускать ниже абсолютного нуля.
Реализовать
- __init__(celsius: float)
- property celsius (getter/setter): при value < -273.15 — ValueError.
- property fahrenheit (read-only): вычисляется из celsius.
Ожидаемый результат — Примеры (doctest)
```python
>>> t = Temperature(0); t.fahrenheit
32.0
>>> t.celsius = 100; t.fahrenheit
212.0
>>> t.celsius = -300  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
ValueError: ...
```

5) Counter — счётчик созданных экземпляров
Что нужно сделать
- Подсчитывать, сколько экземпляров класса было создано.
Реализовать
- Атрибут класса total_created: int, изначально 0.
- В __init__ инкрементировать total_created.
Ожидаемый результат — Примеры (doctest)
```python
>>> Counter(); Counter(); Counter.total_created
2
```

6) Notebook — контейнер заметок
Что нужно сделать
- Хранить строки-заметки и предоставлять базовые операции контейнера.
Реализовать
- add(note: str) -> None
- __len__() -> int
- __iter__() -> Iterator[str]
- __getitem__(idx: int) -> str
Ожидаемый результат — Примеры (doctest)
```python
>>> nb = Notebook(); nb.add('a'); nb.add('b'); len(nb)
2
>>> list(nb)
['a', 'b']
>>> nb[1]
'b'
```

Часть B — Средний уровень

1) Shape — фигуры и площадь
Что нужно сделать
- Общий интерфейс площади и сравнение фигур по площади.
Реализовать
- ABC Shape с abstract area() -> float.
- Классы Rectangle, Circle(r: float), Triangle(b: float, h: float), реализующие area().
- Порядок сравнения по площади (использовать functools.total_ordering).
Ожидаемый результат — Примеры (doctest)
```python
>>> Rectangle(2, 3) < Circle(2)
True
```

2) Polynomial — полиномы
Что нужно сделать
- Хранить коэффициенты и уметь: вычислять значение, складывать и перемножать полиномы.
Реализовать
- __init__(coeffs: list[float]) — coeffs = [c0, c1, c2, ...].
- __call__(x: float) -> float — значение полинома в точке x (схема Горнера).
- __add__(other: Polynomial) -> Polynomial
- __mul__(other: Polynomial) -> Polynomial
- __repr__ -> str
Ожидаемый результат — Примеры (doctest)
```python
>>> Polynomial([1, 1])(2)
3.0
>>> (Polynomial([1, 1]) + Polynomial([0, 2]))(2)
5.0
```

3) RangeLike — «почти range»
Что нужно сделать
- Итерацию по целым, получение длины и индексацию.
Реализовать
- Конструктор как у range: RangeLike(stop) или RangeLike(start, stop, step=1) (step != 0).
- __iter__(), __len__(), __getitem__(idx: int) — поддержать отрицательные индексы, как у списка.
Ожидаемый результат — Примеры (doctest)
```python
>>> rl = RangeLike(1, 5); list(rl)
[1, 2, 3, 4]
>>> rl[0], rl[-1]
(1, 4)
```

4) Warehouse — склад
Что нужно сделать
- Хранить остатки товаров, выдавать по запросу, ругаться при нехватке.
Реализовать
- Класс ошибки NotEnoughStock.
- add(name: str, qty: int) — qty > 0.
- take(name: str, qty: int) — qty > 0, если не хватает — NotEnoughStock; обнулившийся товар удалять из каталога.
- __contains__(name: str) -> bool, __len__() -> int (число позиций).
Ожидаемый результат — Примеры (doctest)
```python
>>> w = Warehouse(); w.add('A', 5); ('A' in w, len(w))
(True, 1)
>>> w.take('A', 3); 'A' in w
True
>>> w.take('A', 2); 'A' in w
False
>>> w.take('A', 1)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotEnoughStock: ...
```

5) JsonReprMixin + Product — сериализация в JSON
Что нужно сделать
- Добавить объекту метод to_json() без изменения базовой логики.
Реализовать
- Mixin JsonReprMixin с методом to_json() -> str (сериализует __dict__).
- Класс Product(name: str, price: float), унаследованный от миксина.
Ожидаемый результат — Примеры (doctest)
```python
>>> Product('A', 10).to_json()
'{"name": "A", "price": 10}'
```

6) Timer — измерение времени
Что нужно сделать
- Измерять время выполнения блока кода через with.
Реализовать
- Контекстный менеджер: __enter__/__exit__, атрибут dt с длительностью.
Ожидаемый результат — Примеры (doctest)
```python
>>> with Timer() as t: _ = sum(range(1000))
>>> t.dt > 0
True
```

Часть C — Продвинутый уровень

1) NonNegative — дескриптор «неотрицательное»
Что нужно сделать
- Запретить запись отрицательных значений в поля.
Реализовать
- Класс-дескриптор NonNegative.
- Пример: class Product: price = NonNegative(); qty = NonNegative().
Ожидаемый результат — Примеры (doctest)
```python
>>> p = Product('A', 10.0, 5); p.price = 0; p.qty = 3
>>> (p.price, p.qty)
(0, 3)
>>> p.price = -1  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
ValueError: ...
```

2) Платёжные стратегии (Strategy + ABC)
Что нужно сделать
- Разные способы оплаты, вызываемые единообразно.
Реализовать
- ABC Payment с pay(amount: float) -> None.
- Реализации: CardPayment, CashPayment, CryptoPayment.
- Функция checkout(amount: float, method: Payment) -> None.
Ожидаемый результат — Примеры (doctest)
```python
>>> checkout(100, CardPayment())
Оплата картой на сумму 100
```

3) EventBus — шина событий
Что нужно сделать
- Подписка/отписка обработчиков и публикация событи��.
Реализовать
- subscribe(event: str, handler: Callable)
- unsubscribe(event: str, handler: Callable)
- publish(event: str, payload: Any)
Ожидаемый результат — Примеры (doctest)
```python
>>> bus = EventBus(); out = []
>>> bus.subscribe('tick', lambda x: out.append(x))
>>> bus.publish('tick', 1); out
[1]
```

4) Settings — настройки с заморозкой
Что нужно сделать
- После freeze() любые изменения запрещены.
Реализовать
- __slots__ = ("host", "port", "debug", "_frozen").
- freeze(): помечает объект замороженным.
- __setattr__: при _frozen=True поднимает FrozenError.
Ожидаемый результат — Примеры (doctest)
```python
>>> s = Settings(); s.host = '127.0.0.1'; s.freeze()
>>> s.port = 9000  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
FrozenError: ...
```

Сдача
- Структура: src/ (код) и tests/ (по желанию). Или один файл с doctest-примерами.
- В README коротко опишите, как запустить проверки.
