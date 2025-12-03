from modules.lighting.lighting_module import LightingModule
from modules.transport.transport_module import TransportModule
from modules.security.security_module import SecurityModule
from modules.energy.energy_module import EnergyModule

class ModuleFactory:
    @staticmethod
    def create_module(name: str, config: dict = None):
        name = name.lower()
        if name == "lighting":
            return LightingModule()
        if name == "transport":
            return TransportModule()
        if name == "security":
            return SecurityModule()
        if name == "energy":
            return EnergyModule()

        raise ValueError("❌ Unknown module")
