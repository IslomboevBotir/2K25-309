from abc import ABC, abstractmethod

class SystemFactory(ABC):
    @abstractmethod
    def create_system(self): pass

class TransportFactory(SystemFactory):
    def create_system(self):
        print("[Factory] Transport tizimi yaratildi")
        from modules.transport import TransportSystem
        return TransportSystem()

class LightingFactory(SystemFactory):
    def create_system(self):
        print("[Factory] Yoritish tizimi yaratildi")
        from modules.lighting import LightingSystem
        return LightingSystem()

class EnergyFactory(SystemFactory):
    def create_system(self):
        print("[Factory] Energiya tizimi yaratildi")
        from modules.energy import EnergySystem
        return EnergySystem()