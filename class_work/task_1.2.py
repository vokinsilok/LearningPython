# python
class Account:
    def __init__(self, balance: float = 0.0):
        self.__balance = float(balance)

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = float(value)

    def __repr__(self) -> str:
        return f"Account(balance={self.__balance:.2f})"

account = Account(234.56)
print(account.balance)
# print(account._balance)


account.deposit(100.0)
print(account.balance)
# print(account._balance)


account.balance = 500.0
print(account.balance)
# print(account._balance)

print(account)