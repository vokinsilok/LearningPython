class Account:
    def __init__(self, balance: float = 0.0):
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def add_balance(self, amount: float):
        self._balance += amount

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value


account = Account(234.56)
print(account.balance)
print(account._balance)


account.add_balance(100.0)
print(account.balance)
print(account._balance)


account.balance = 500.0
print(account.balance)
print(account._balance)

print(account)