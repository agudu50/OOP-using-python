# Nurse.py
from MedicalPersonnel import MedicalPersonnel

class Nurse(MedicalPersonnel):
    def __init__(self, name: str, id: str, department: str):
        super().__init__(name, id)
        self._department = department

    def perform_duties(self) -> None:
        print(f"Nurse {self.get_name()} provides patient care, administers medications, and assists doctors.")

    def get_specialization(self) -> str:
        return self._department

    def __str__(self) -> str:
        return f"Specialization: {self.get_specialization()}"