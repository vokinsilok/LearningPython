class Counter:
    __total_created = 0

    def __init__(self) -> None:
        Counter.__total_created += 1

    @property
    def total_created(self) -> int:
        return self.__total_created


a = Counter()
b = Counter()
Counter()
Counter()
q = a.total_created
print(q)
