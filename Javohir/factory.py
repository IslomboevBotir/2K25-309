from modules.lighting import LightingSystem
from modules.transport import TransportSystem
from modules.security import SecuritySystem
from modules.energy import EnergySystem


class ModuleFactory:
    """
    Factory Method — turli shahar modullarini yaratadi
    """
    @staticmethod
    def create(name):
        if name == "lighting":
            return LightingSystem()
        if name == "transport":
            return TransportSystem()
        if name == "security":
            return SecuritySystem()
        if name == "energy":
            return EnergySystem()
        raise Exception("Bunday modul topilmadi")
