# main.py
try:
    from pharmacist import Pharmacist
except ImportError:
    print("Error: pharmacist_module could not be resolved")
from nurse_module import Nurse  # Add this import statement
try:
    from doctor_module import Doctor
except ImportError:
    print("Error: doctor_module could not be resolved")

if __name__ == "__main__":
    personnel = [
        Doctor("Dr. Anthony Gudu", "D001", "Cardiologist"),
        Nurse("Kessiah Gudu", "N522", "Emergency"),
        Pharmacist("Daniel Gudu", "D642", "PHL00585")
    ]

    for person in personnel:
        person.display_details()
        person.perform_duties()
        print(person.get_specialization())
        print()
