class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"

account = Account("Alice", 100)

print(account)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)
account.withdraw(-10)

print(account)