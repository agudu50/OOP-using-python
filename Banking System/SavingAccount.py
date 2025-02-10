# SavingsAccount.py
from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name: str, account_number: str, balance: float, interest_rate: float):
        super().__init__(account_holder_name, account_number, balance)
        self._interest_rate = interest_rate

    def withdraw(self, amount: float) -> None:
        if self.get_balance() - amount >= 100:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawal successful. New balance: GHS {self.get_balance()}")
        else:
            print("Minimum balance requirement not met.")

    def calculate_interest(self) -> None:
        interest = self.get_balance() * (self._interest_rate / 100)
        print(f"Annual Interest: GHS {interest}")

    def display_account_details(self) -> None:
        super().display_account_details()
        print(f"Interest Rate: {self._interest_rate}%")

    def display_accoun_details(self) -> None:
        pass
