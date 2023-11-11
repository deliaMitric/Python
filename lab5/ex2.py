class Account:
    def __init__(self, acc_number, holder, balance):
        self._number = acc_number
        self._holder = holder
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            return "Invalid amount!!!"
        self._balance += amount
        print(f"Current balance: {self._balance}")

    def withdraw(self, amount):
        if amount < 0 or amount > self._balance:
            return "Invalid amount!!!"
        self._balance -= amount

    def interest_calculation(self):
        pass

class SavingsAccount(Account):
    def __init__(self, acc_number, holder, balance, interest_percent=0.05):
        super().__init__(acc_number, holder, balance)
        self._interest_percent = interest_percent

    def interest_calculation(self):
        self._balance += (self._interest_percent * self._balance)
        print(f"New balance is: {self._balance}")

class CheckingAccount(Account):
    def __init__(self, acc_number, holder, balance, overdraft_limit=0):
        super().__init__(acc_number, holder, balance)
        self._overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount > 0  and amount < self._balance + self._overdraft_limit:
            self._balance -= amount
            print(f"Current balance is: {self._balance}")

if __name__ == '__main__':
    list = [SavingsAccount(1239, "Delia", 0, 0.004), CheckingAccount(89760, "Alice", 50, 300)]
    for account in list:
        account.deposit(340)
