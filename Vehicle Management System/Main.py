class RentalManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_available_vehicles(self):
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(vehicle)

    def rent_vehicle_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                vehicle.is_available = False
                print(f"Vehicle {vehicle_id} has been rented.")
                return
        print(f"Vehicle {vehicle_id} is not available.")

    def return_vehicle_by_id(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id and not vehicle.is_available:
                vehicle.is_available = True
                print(f"Vehicle {vehicle_id} has been returned.")
                return
        print(f"Vehicle {vehicle_id} was not rented.")

class Vehicle:
    def __init__(self, vehicle_id, brand, model, is_available):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.is_available = is_available

    def __str__(self):
        return f"{self.brand} {self.model} (ID: {self.vehicle_id})"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, is_available, seating_capacity):
        super().__init__(vehicle_id, brand, model, is_available)
        self.seating_capacity = seating_capacity

    def calculate_rental_cost(self, days):
        return days * 50  # Example cost calculation

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, is_available, engine_capacity):
        super().__init__(vehicle_id, brand, model, is_available)
        self.engine_capacity = engine_capacity

    def calculate_rental_cost(self, days):
        return days * 30  # Example cost calculation

if __name__ == "__main__":
    rental_manager = RentalManager()

    car1 = Car("C001", "Toyota", "Camry", True, 5)
    car2 = Car("C002", "Honda", "Accord", True, 4)
    bike1 = Bike("B001", "Yamaha", "R15", True, 150)
    bike2 = Bike("B002", "Kawasaki", "Ninja", True, 200)

    rental_manager.add_vehicle(car1)
    rental_manager.add_vehicle(car2)
    rental_manager.add_vehicle(bike1)
    rental_manager.add_vehicle(bike2)

    print("Available Vehicles:")
    rental_manager.display_available_vehicles()

    print("\nRenting vehicle C001...")
    rental_manager.rent_vehicle_by_id("C001")

    print("\nAvailable Vehicles after renting C001:")
    rental_manager.display_available_vehicles()

    print("\nReturning vehicle C001...")
    rental_manager.return_vehicle_by_id("C001")

    print("\nAvailable Vehicles after returning C001:")
    rental_manager.display_available_vehicles()

    print(f"\nRental cost for car C001 for 5 days: GHS {car1.calculate_rental_cost(5)}")
    print(f"Rental cost for bike B001 for 3 days: GHS {bike1.calculate_rental_cost(3)}")
