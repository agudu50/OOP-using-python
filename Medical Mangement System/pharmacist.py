# Pharmacist.py
from MedicalPersonnel import MedicalPersonnel

class Pharmacist(MedicalPersonnel):
    def __init__(self, name: str, id: str, pharmacist_license_id: str):
        super().__init__(name, id)
        self._pharmacist_license_id = pharmacist_license_id

    def perform_duties(self) -> None:
        print(f"Pharmacist {self.get_name()} dispenses medication and advises patients on drug usage.")

    def get_specialization(self) -> str:
        return "Pharmacy"

    def __str__(self) -> str:
        return f"Specialization: {self.get_specialization()}"