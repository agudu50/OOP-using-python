from abc import ABC, abstractmethod

# BankAccount.py (Abstract Base Class)
class BankAccount(ABC):
    def __init__(self, account_holder_name: str, account_number: str, balance: float):
        self._account_holder_name = account_holder_name
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount: float, transaction_note: str = "") -> None:
        self._balance += amount
        note = f"{transaction_note} " if transaction_note else ""
        print(f"Deposited successfully. {note}New balance is: GHS {self._balance}")

    def withdraw(self, amount: float) -> None:
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal successful. New balance is: GHS {self._balance}")
        else:
            print("Insufficient funds.")

    def display_account_details(self) -> None:
        print(f"Account Holder Name: {self._account_holder_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: GHS {self._balance}")

    def get_balance(self) -> float:
        return self._balance

    def set_balance(self, balance: float) -> None:
        self._balance = balance

    @abstractmethod
    def display_accoun_details(self) -> None:
        pass
