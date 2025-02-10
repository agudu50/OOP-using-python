from abc import ABC, abstractmethod

# Vehicle.py (Abstract Base Class)
class Vehicle(ABC):
    def __init__(self, vehicle_id: str, brand: str, model: str, is_available: bool):
        self._vehicle_id = vehicle_id
        self._brand = brand
        self._model = model
        self._is_available = is_available

    def get_vehicle_id(self) -> str:
        return self._vehicle_id

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def is_available(self) -> bool:
        return self._is_available

    def rent_vehicle(self) -> None:
        if self._is_available:
            self._is_available = False
        else:
            raise Exception("Vehicle is not available for rent.")

    def return_vehicle(self) -> None:
        self._is_available = True

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        pass
