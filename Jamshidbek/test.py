import os
import sys
import unittest

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(THIS_DIR)
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from Jamshidbek.core.builders.city_builder import CityConfigBuilder
from Jamshidbek.core.controller import SmartCityController


class TestSmartCity(unittest.TestCase):
    def setUp(self):
        cfg = (
            CityConfigBuilder()
            .city_name("TestCity")
            .zones_count(1)
            .eco_mode(True)
            .default_role("guest")
            .build()
        )
        self.c1 = SmartCityController(cfg)

    def test_singleton(self):
        cfg2 = (
            CityConfigBuilder()
            .city_name("AnotherCity")
            .zones_count(1)
            .eco_mode(False)
            .default_role("guest")
            .build()
        )
        c2 = SmartCityController(cfg2)
        self.assertIs(self.c1, c2)

    def test_proxy_guest_denied(self):
        self.c1.set_role("guest")
        self.assertIn("denied", self.c1.security_arm().lower())

    def test_proxy_admin_allowed(self):
        self.c1.set_role("admin")
        self.assertIn("armed", self.c1.security_arm().lower())

    def test_decorator_eco_cap(self):
        msg = self.c1.lighting_brightness(100)
        self.assertIn("eco", msg.lower())

    def test_adapter_weather_present(self):
        status = self.c1.city_status().lower()
        self.assertIn("weather in", status)


if __name__ == "__main__":
    unittest.main()
