from abc import ABC, abstractmethod

# MedicalPersonnel.py
class MedicalPersonnel(ABC):
    def __init__(self, name: str, id: str):
        self._name = name
        self._id = id

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> str:
        return self._id

    def display_details(self) -> None:
        print(f"Name: {self._name}, ID: {self._id}")

    @abstractmethod
    def perform_duties(self) -> None:
        pass

    @abstractmethod
    def get_specialization(self) -> str:
        pass
