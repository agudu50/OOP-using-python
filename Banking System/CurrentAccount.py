# CurrentAccount.py
from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_holder_name: str, account_number: str, balance: float, overdraft_limit: float):
        super().__init__(account_holder_name, account_number, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if self.get_balance() - amount >= -self._overdraft_limit:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawal successful. New balance: GHS {self.get_balance()}")
        else:
            print("Overdraft limit exceeded.")

    def display_account_details(self) -> None:
        super().display_account_details()
        print(f"Overdraft Limit: GHS {self._overdraft_limit}")

    def display_accoun_details(self) -> None:
        pass