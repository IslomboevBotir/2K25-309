"""
Factory Method Pattern - creates objects without specifying exact class
Used for: Creating different types of transport vehicles
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass


class Bus(Vehicle):
    def __init__(self, route_number):
        self.route_number = route_number
        self.passengers = 0
    
    def move(self):
        return f"🚌 Bus #{self.route_number} is moving with {self.passengers} passengers"
    
    def get_status(self):
        return f"Bus #{self.route_number}: {self.passengers}/50 passengers"


class Tram(Vehicle):
    def __init__(self, line):
        self.line = line
        self.is_operational = True
    
    def move(self):
        return f"🚋 Tram on line {self.line} is operating"
    
    def get_status(self):
        status = "Operational" if self.is_operational else "Maintenance"
        return f"Tram Line {self.line}: {status}"


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, identifier):
        pass


class BusFactory(VehicleFactory):
    def create_vehicle(self, route_number):
        return Bus(route_number)


class TramFactory(VehicleFactory):
    def create_vehicle(self, line):
        return Tram(line)