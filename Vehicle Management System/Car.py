# Car.py
from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, model: str, is_available: bool, seating_capacity: int):
        super().__init__(vehicle_id, brand, model, is_available)
        self._seating_capacity = seating_capacity

    def calculate_rental_cost(self, days: int) -> float:
        return 1000 * days + self._seating_capacity * 50

# Bike.py
class Bike(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, model: str, is_available: bool, engine_capacity: int):
        super().__init__(vehicle_id, brand, model, is_available)
        self._engine_capacity = engine_capacity

    def calculate_rental_cost(self, days: int) -> float:
        return 500 * days + self._engine_capacity * 10