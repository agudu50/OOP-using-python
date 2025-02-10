# Doctor.py
from MedicalPersonnel import MedicalPersonnel

class Doctor(MedicalPersonnel):
    def __init__(self, name: str, id: str, specialization: str):
        super().__init__(name, id)
        self._specialization = specialization

    def perform_duties(self) -> None:
        print(f"Doctor {self.get_name()} diagnoses patients, prescribes medication, and conducts surgeries.")

    def get_specialization(self) -> str:
        return self._specialization

    def __str__(self) -> str:
        return f"Specialization: {self.get_specialization()}"