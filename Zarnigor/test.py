"""
Unit tests for SmartCity System using unittest.
Covers Singleton, Factory, Builder, Adapter, Proxy, and subsystem behaviors.
"""

import unittest

from core.controller import SmartCityController
from core.singleton.logger import Logger
from core.factories.factory import SubsystemFactory
from core.builders.builder import CityReportBuilder, CityReportDirector
from core.adapters.adapter import WeatherServiceAdapter
from core.proxy.proxy import SecurityProxy, LightingProxy

from modules.transport.transport import TransportSystem
from modules.lighting.lighting import LightingSystem, BasicLight, LightGroup, LoggingDecorator
from modules.security.security import SecuritySystem
from modules.energy.energy import EnergySystem


class TestSmartCitySystem(unittest.TestCase):

    def test_singleton_controller(self):
        c1 = SmartCityController()
        c2 = SmartCityController()
        self.assertIs(c1, c2, "SmartCityController must be a Singleton")

    def test_singleton_logger(self):
        l1 = Logger()
        l2 = Logger()
        self.assertIs(l1, l2, "Logger must be a Singleton")

    def test_factory_creates_subsystems(self):
        factory = SubsystemFactory()
        self.assertIsInstance(factory.create_transport_system(), TransportSystem)
        self.assertIsInstance(factory.create_lighting_system(), LightingSystem)
        self.assertIsInstance(factory.create_security_system(), SecuritySystem)
        self.assertIsInstance(factory.create_energy_system(), EnergySystem)

    def test_subsystem_status_methods(self):
        transport = TransportSystem()
        lighting = LightingSystem()
        security = SecuritySystem()
        energy = EnergySystem()

        self.assertIn("Transport", transport.get_status())
        self.assertIn("Lighting system", lighting.get_status())
        self.assertIn("Security", security.get_status())
        self.assertIn("Energy", energy.get_status())

    def test_builder_report_contains_sections(self):
        builder = CityReportBuilder()
        director = CityReportDirector(builder)

        director.build_full_report(
            transport_status="Transport OK",
            lighting_status="Lighting OK",
            security_status="Security OK",
            energy_status="Energy OK",
        )

        report = builder.get_result()
        self.assertIn("SmartCity Daily Report", report)
        self.assertIn("Transport status", report)
        self.assertIn("Lighting status", report)
        self.assertIn("Security status", report)
        self.assertIn("Energy status", report)

    def test_adapter_weather_returns_text(self):
        adapter = WeatherServiceAdapter()
        weather = adapter.get_weather_info()
        self.assertIn("°", weather)
        self.assertTrue(len(weather) > 0)

    def test_security_proxy_access(self):
        security = SecuritySystem()
        proxy = SecurityProxy(security)

        admin_access = proxy.access("admin")
        user_access = proxy.access("user")

        self.assertIn("ADMIN ACCESS GRANTED", admin_access)
        self.assertIn("ACCESS DENIED", user_access)

    def test_lighting_proxy_access(self):
        lighting = LightingSystem()
        proxy = LightingProxy(lighting)

        # admin can turn on
        proxy.turn_all_on("admin")
        for child in lighting.root_group.children:
            # each child is a LoggingDecorator wrapping BasicLight
            self.assertTrue(child.wrapped.is_on)

        # user cannot turn off
        proxy.turn_all_off("user")  # should not change state
        for child in lighting.root_group.children:
            self.assertTrue(child.wrapped.is_on)

    def test_lighting_composite_and_decorator(self):
        root_group = LightGroup("Test Group")
        l1 = LoggingDecorator(BasicLight(1))
        l2 = LoggingDecorator(BasicLight(2))
        root_group.add(l1)
        root_group.add(l2)

        root_group.turn_on()
        self.assertTrue(l1.wrapped.is_on)
        self.assertTrue(l2.wrapped.is_on)

        root_group.turn_off()
        self.assertFalse(l1.wrapped.is_on)
        self.assertFalse(l2.wrapped.is_on)


if __name__ == "__main__":
    unittest.main()
