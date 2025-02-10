from Vehicle import Vehicle

class RentalManager:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def display_available_vehicles(self) -> None:
        for vehicle in self._vehicles:
            if vehicle.is_available():
                print(f"Vehicle ID: {vehicle.get_vehicle_id()}, Brand: {vehicle.get_brand()}, Model: {vehicle.get_model()}")

    def rent_vehicle_by_id(self, vehicle_id: str) -> None:
        for vehicle in self._vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                try:
                    vehicle.rent_vehicle()
                    print("Vehicle rented successfully.")
                    return
                except Exception as e:
                    print(e)
                    return
        print(f"Vehicle with ID {vehicle_id} not found.")

    def return_vehicle_by_id(self, vehicle_id: str) -> None:
        for vehicle in self._vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                vehicle.return_vehicle()
                print("Vehicle returned successfully.")
                return
        print(f"Vehicle with ID {vehicle_id} not found.")
