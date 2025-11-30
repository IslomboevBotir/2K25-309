import unittest
from modules.lighting.lighting_factory import LightingSystemFactory
from modules.lighting.lights import SolarLight, LEDLight

class TestAbstractFactory(unittest.TestCase):
    def test_eco_system_uses_solar(self):
        system = LightingSystemFactory.create_system("eco")
        self.assertIsInstance(system.impl, SolarLight)

    def test_standard_system_uses_led(self):
        system = LightingSystemFactory.create_system("standard")
        self.assertIsInstance(system.impl, LEDLight)

    def test_eco_turn_on_includes_message(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            system = LightingSystemFactory.create_system("eco")
            system.turn_on()
            mock_print.assert_any_call("🌿 Eco Mode: Optimizing light usage...")