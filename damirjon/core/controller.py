# controller.py
# PATTERN: Facade – barcha modullarni yagona nuqtadan boshqaradi.
# PATTERN: Singleton – Controller bitta nusxada ishlaydi.

from core.singleton import Singleton
from modules.lighting import LightingSystem
from modules.transport import TransportSystem
from modules.security import SecuritySystem
from modules.energy import EnergySystem

class SmartCityController(metaclass=Singleton):
    """Facade + Singleton controller"""

    def __init__(self):
        self.lighting = LightingSystem()
        self.transport = TransportSystem()
        self.security = SecuritySystem()
        self.energy = EnergySystem()

    def start_system(self):
        print("\n--- SmartCity Started ---")
        self.lighting.turn_on_lights()
        self.transport.manage_traffic()
        self.security.scan_area()
        self.energy.optimize_energy()
        print("--- All systems operational ---\n")
