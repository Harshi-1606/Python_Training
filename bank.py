class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit: {amount}, New Balance: {self.balance}"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdraw: {amount}, New Balance: {self.balance}"
            else:
                return "Insufficient funds"
        else:
            return "Withdraw amount must be positive"

    def display_balance(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: {interest}, New Balance: {self.balance}"

owner = input("Enter account owner's name: ")
balance = float(input("Enter initial balance: "))
interest_rate = float(input("Enter interest rate (e.g. 0.05 for 5%): "))

savings = SavingsAccount(owner, balance, interest_rate)

while True:
    print("\nChoose an action:")
    print("1: Display balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Apply interest")
    print("5: Exit")
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        print(savings.display_balance())
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        print(savings.deposit(amount))
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        print(savings.withdraw(amount))
    elif choice == "4":
        print(savings.apply_interest())
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
