class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if (self._balance - amount) < 0:
            print('Not enough money!')
            return
        self._balance -= amount

    def get_balance(self):
        print(self._balance)

acc = BankAccount()
acc.withdraw(100)
acc.deposit(100)
acc.withdraw(50)
acc.get_balance()

