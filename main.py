class Account:
    def __init__(self, acc_no, owner, balance=0):
        self.acc_no = acc_no
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            return True
        return False


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account):
        self.accounts[account.acc_no] = account

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].withdraw(amount):
                self.accounts[to_acc].deposit(amount)
                return "Transfer success"
        return "Failed"


bank = Bank()

a1 = Account(1, "Ali", 500)
a2 = Account(2, "John", 300)

bank.create_account(a1)
bank.create_account(a2)

print(bank.transfer(1, 2, 200))
print(a1.balance, a2.balance)
