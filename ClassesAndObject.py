class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. Balance = {self.balance}")
        else:
            print("Insufficient funds")

# Using the class
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.deposit(200)   # Alice deposited 200. Balance = 1200
acc2.withdraw(100)  # Bob withdrew 100. Balance = 400
