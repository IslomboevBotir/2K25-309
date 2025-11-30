# FIO/core/builders/infrastructure_builder.py

from abc import ABC, abstractmethod

# --- Product ---
class CityInfrastructure:
    """The complex object being constructed."""
    def __init__(self):
        self.parts = {}

    def add_part(self, name, specification):
        self.parts[name] = specification

    def show_configuration(self):
        print("\n--- City Infrastructure Configuration ---")
        for part, spec in self.parts.items():
            print(f"- {part}: {spec}")
        print("---------------------------------------")

# --- Builder Interface ---
class InfrastructureBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_transport_network(self):
        pass

    @abstractmethod
    def build_smart_grid(self):
        pass

    @abstractmethod
    def build_security_perimeter(self):
        pass

    @abstractmethod
    def get_result(self) -> CityInfrastructure:
        pass

# --- Concrete Builder ---
class SmartCityBuilder(InfrastructureBuilder):
    """
    Design Pattern: Builder (Creational)
    Purpose: Separates the construction of a complex object (CityInfrastructure) from its
             representation, allowing the same construction process to create different representations.
    Usage: Used to construct a new city infrastructure project step-by-step.
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self._infrastructure = CityInfrastructure()

    def build_transport_network(self):
        self._infrastructure.add_part("Transport Network", "Integrated traffic light system and tram lines.")

    def build_smart_grid(self):
        self._infrastructure.add_part("Smart Grid", "Decentralized energy management with solar integration.")

    def build_security_perimeter(self):
        self._infrastructure.add_part("Security Perimeter", "AI-powered surveillance and rapid response units.")

    def get_result(self) -> CityInfrastructure:
        infrastructure = self._infrastructure
        self.reset() # Reset the builder for the next construction
        return infrastructure

# --- Director (Optional, but useful for common construction processes) ---
class InfrastructureDirector:
    """The Director knows the steps to build a specific configuration."""
    def __init__(self, builder: InfrastructureBuilder):
        self._builder = builder

    def build_minimal_infrastructure(self):
        self._builder.build_transport_network()

    def build_full_infrastructure(self):
        self._builder.build_transport_network()
        self._builder.build_smart_grid()
        self._builder.build_security_perimeter()
