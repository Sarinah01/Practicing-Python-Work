class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive!")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")


# --- Driver Code ---
def main():
    print("🏦 Welcome to Python Bank 🏦")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for banking with us! 👋")
            break
        else:
            print("Invalid choice! Please try again.")

main()
