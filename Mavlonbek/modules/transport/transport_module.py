# FIO/modules/transport/transport_module.py

from abc import ABC, abstractmethod

# --- Product Interface ---
class Vehicle(ABC):
    @abstractmethod
    def operate(self):
        pass

# --- Concrete Products ---
class Bus(Vehicle):
    def operate(self):
        return "Bus is operating on route 101."

class Tram(Vehicle):
    def operate(self):
        return "Tram is operating on the central line."

class Taxi(Vehicle):
    def operate(self):
        return "Taxi is available for on-demand service."

# --- Creator (Factory Method) ---
class TransportModule:
    """
    Design Pattern: Factory Method (Creational)
    Purpose: Defines an interface for creating an object (Vehicle), but lets subclasses
             (or a method within the class) decide which class to instantiate.
    Usage: The create_vehicle method acts as the factory, allowing the system to easily
           add new vehicle types without modifying the core module logic.
    """
    def __init__(self):
        self.vehicles = []

    def _factory_method(self, vehicle_type: str) -> Vehicle:
        """The actual factory method."""
        if vehicle_type.lower() == "bus":
            return Bus()
        elif vehicle_type.lower() == "tram":
            return Tram()
        elif vehicle_type.lower() == "taxi":
            return Taxi()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

    def create_vehicle(self, vehicle_type: str):
        try:
            vehicle = self._factory_method(vehicle_type)
            self.vehicles.append(vehicle)
            print(f"Transport Module: Created and deployed a new {vehicle_type.capitalize()}.")
            print(f"Operation: {vehicle.operate()}")
        except ValueError as e:
            print(f"Transport Module Error: {e}")

    def start_traffic_control(self):
        print("Transport Module: Traffic control system activated.")

    def get_status(self):
        print(f"Transport Module Status: {len(self.vehicles)} vehicles currently deployed.")
