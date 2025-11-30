# FIO/core/factories/abstract_factory.py

from abc import ABC, abstractmethod

# --- Abstract Products ---

class Sensor(ABC):
    """Abstract Product A: Sensor"""
    @abstractmethod
    def monitor(self):
        pass

class Actuator(ABC):
    """Abstract Product B: Actuator"""
    @abstractmethod
    def actuate(self):
        pass

# --- Concrete Products (Type 1: Basic) ---

class BasicTrafficSensor(Sensor):
    def monitor(self):
        return "Monitoring basic traffic flow."

class BasicStreetLight(Actuator):
    def actuate(self):
        return "Adjusting basic street light intensity."

# --- Concrete Products (Type 2: Advanced) ---

class AdvancedTrafficSensor(Sensor):
    def monitor(self):
        return "Monitoring advanced traffic flow with AI analysis."

class AdvancedStreetLight(Actuator):
    def actuate(self):
        return "Adjusting advanced street light color and intensity."

# --- Abstract Factory ---

class CityDeviceFactory(ABC):
    """
    Design Pattern: Abstract Factory (Creational)
    Purpose: Provides an interface for creating families of related or dependent objects
             (Sensors and Actuators) without specifying their concrete classes.
    Usage: Allows the system to switch between 'Basic' and 'Advanced' device configurations easily.
    """
    @abstractmethod
    def create_sensor(self) -> Sensor:
        pass

    @abstractmethod
    def create_actuator(self) -> Actuator:
        pass

# --- Concrete Factories ---

class BasicDeviceFactory(CityDeviceFactory):
    def create_sensor(self) -> Sensor:
        return BasicTrafficSensor()

    def create_actuator(self) -> Actuator:
        return BasicStreetLight()

class AdvancedDeviceFactory(CityDeviceFactory):
    def create_sensor(self) -> Sensor:
        return AdvancedTrafficSensor()

    def create_actuator(self) -> Actuator:
        return AdvancedStreetLight()
