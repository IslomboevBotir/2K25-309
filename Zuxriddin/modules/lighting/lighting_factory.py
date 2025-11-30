from .lights import LEDLight, SolarLight
from core.subsystems import LightingSystem

class EcoLightingSystem(LightingSystem):
    def turn_on(self):
        print("🌿 Eco Mode: Optimizing light usage...")
        self.impl.turn_on()

    def turn_off(self):
        self.impl.turn_off()
        print("🌿 Eco Mode: Lights off to save energy.")

class StandardLightingSystem(LightingSystem):
    def turn_on(self):
        print("🏙️ Standard Mode: Full brightness.")
        self.impl.turn_on()

    def turn_off(self):
        self.impl.turn_off()

class LightingSystemFactory:
    """Abstract Factory: Creates families of related lighting products."""
    @staticmethod
    def create_system(system_type="eco"):
        if system_type == "eco":
            return EcoLightingSystem(SolarLight())
        else:
            return StandardLightingSystem(LEDLight())