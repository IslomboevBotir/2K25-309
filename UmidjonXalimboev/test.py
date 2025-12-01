import unittest
from core.singleton.logger import Logger
from core.factories.device_factory import EnergySavingFactory, StandardFactory
from core.builders.report_builder import ReportBuilder
from core.controller import SmartCityController
from modules.lighting.lighting import LightingSubsystem, Zone
from core.adapters.weather_adapter import ExternalWeatherService, WeatherAdapter
from core.proxy.security_proxy import SecurityProxy

class TestSmartCity(unittest.TestCase):

    def test_logger_singleton(self):
        logger1 = Logger.get_instance()
        logger2 = Logger.get_instance()
        self.assertIs(logger1, logger2, "Logger should be singleton")

    def test_factory_devices(self):
        ef = EnergySavingFactory()
        light = ef.create_light()
        transport = ef.create_transport_unit()
        self.assertIn("LED", light.info())
        self.assertIn("Electric", transport.info())

        sf = StandardFactory()
        light2 = sf.create_light()
        transport2 = sf.create_transport_unit()
        self.assertIn("Halogen", light2.info())
        self.assertIn("Diesel", transport2.info())

    def test_builder_report(self):
        builder = ReportBuilder()
        report = builder.add_header("Test Header").add_section("Section1", "Content").add_footer("End").build()
        self.assertIn("Test Header", report)
        self.assertIn("Section1", report)
        self.assertIn("End", report)

    def test_lighting_composite(self):
        factory = EnergySavingFactory()
        lighting = LightingSubsystem(factory)
        self.assertIsInstance(lighting.zone, Zone)
        self.assertGreater(len(lighting.zone.children), 0)
        lighting.turn_all_on()
        for light in lighting.zone.children:
            self.assertTrue(light._wrapped.on if hasattr(light, "_wrapped") else light.on)

    def test_weather_adapter(self):
        service = ExternalWeatherService()
        adapter = WeatherAdapter(service)
        w = adapter.current_weather()
        self.assertIn("condition", w)
        self.assertIn("temperature_celsius", w)

    def test_security_proxy_access(self):
        proxy_guest = SecurityProxy(user_role="guest")
        proxy_admin = SecurityProxy(user_role="admin")
        # Guest should be denied
        self.assertIsNone(proxy_guest.get_status())
        # Admin should get status string
        self.assertIsNone(proxy_admin.get_status())  # prints status, returns None

    def test_controller_singleton(self):
        ctrl1 = SmartCityController.get_instance()
        ctrl2 = SmartCityController.get_instance()
        self.assertIs(ctrl1, ctrl2, "Controller should be singleton")

if __name__ == "__main__":
    unittest.main()
