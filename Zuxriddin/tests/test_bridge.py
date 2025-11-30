import unittest
from modules.lighting.lighting_factory import EcoLightingSystem, StandardLightingSystem
from modules.lighting.lights import SolarLight, LEDLight

class TestBridge(unittest.TestCase):
    def test_eco_lighting_uses_solar_impl(self):
        impl = SolarLight()
        system = EcoLightingSystem(impl)
        self.assertIs(system.impl, impl)

    def test_standard_lighting_uses_led_impl(self):
        impl = LEDLight()
        system = StandardLightingSystem(impl)
        self.assertIs(system.impl, impl)

    def test_abstraction_and_implementation_decoupled(self):
        # Can swap implementations without changing abstraction logic
        system1 = EcoLightingSystem(SolarLight())
        system2 = EcoLightingSystem(LEDLight())
        self.assertNotEqual(type(system1.impl), type(system2.impl))