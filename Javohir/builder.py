from modules.lighting import LightingSystem
from modules.transport import TransportSystem
from modules.security import SecuritySystem
from modules.energy import EnergySystem

class SmartCityBuilder:
    def __init__(self):
        self.components = {}

    def add_lighting(self):
        self.components["lighting"] = LightingSystem()
        return self

    def add_transport(self):
        self.components["transport"] = TransportSystem()
        return self

    def add_security(self):
        self.components["security"] = SecuritySystem()
        return self

    def add_energy(self):
        self.components["energy"] = EnergySystem()
        return self

    def build(self):
        return self.components
