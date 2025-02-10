 #main.py
class CurrentAccount:
    def __init__(self, account_holder, account_number, balance, overdraft_limit):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount, description=""):
        self.balance += amount
        print(f"Deposited {amount}. {description} New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Overdraft Limit: {self.overdraft_limit}")

class SavingsAccount:
    def __init__(self, account_holder, account_number, balance, interest_rate):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount, description=""):
        self.balance += amount
        print(f"Deposited {amount}. {description} New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Interest: {interest}")

if __name__ == "__main__":
    savings_account = SavingsAccount("Anthony Gudu", "SA12345", 500, 3)
    current_account = CurrentAccount("Anthony Gudu", "CA54321", 1000, 500)

    print("\nSavings Account Deposit:")
    savings_account.deposit(200)
    savings_account.deposit(300, "Salary credited.")

    print("\nCurrent Account Deposit:")
    current_account.deposit(500)
    current_account.deposit(400, "Project payment received.")

    print("\nSavings Account Withdrawal:")
    savings_account.withdraw(450)

    print("\nCurrent Account Withdrawal:")
    current_account.withdraw(1300)
    current_account.withdraw(2000)

    print("\nAccount Details:")
    savings_account.display_account_details()
    savings_account.calculate_interest()

    print()
    current_account.display_account_details()
