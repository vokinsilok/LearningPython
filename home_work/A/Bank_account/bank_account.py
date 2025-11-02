class BankAccount:
    def __init__(self, balance: float=0.0):
        self.__balance = balance

    def add_balance(self, amount: float=0.0):
        if amount < 0:
            raise ValueError('amount cannot be negative')
        self.__balance += amount

    def less_balance(self, amount: float=0.0):
        if amount < 0:
            raise ValueError('amount cannot be negative')
        if amount > self.__balance:
            raise ValueError('amount cannot be greater than balance')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    @property
    def balance(self):
        return self.__balance

account_1 = BankAccount(100)
account_1.less_balance(90)
account_1.add_balance(50)
print(account_1.get_balance())

