import unittest
from core.controller import Controller
from core.factory.factory import ModuleFactory
from core.builder.traffic_builder import TrafficBuilder, TrafficSchedule
from modules.lighting.lighting_module import BasicLight, LightGroup, LoggingDecorator
from modules.transport.transport_module import Vehicle, Transports
from core.adapter.weather_adapter import WeatherAdapter, WeatherProvider


class Test(unittest.TestCase):

    def test_singleton_controller(self):
        """Singleton Pattern Test"""
        c1 = Controller()
        c2 = Controller()
        self.assertTrue(c1 is c2)
        self.assertEqual(id(c1), id(c2))

    def test_facade_system(self):
        """Facade Pattern Test"""
        ctrl = Controller()
        # We only verify that facade exposes subsystems and methods exist
        self.assertTrue(hasattr(ctrl, "lighting"))
        self.assertTrue(hasattr(ctrl, "transport"))
        self.assertTrue(hasattr(ctrl, "security"))
        self.assertTrue(hasattr(ctrl, "energy"))
        self.assertTrue(callable(ctrl.system_status))
        self.assertTrue(callable(ctrl.toggle_city_lights))

    def test_factory_method(self):
        """Factory Method Pattern Test"""
        light_module = ModuleFactory.create_module("lighting")
        transport_module = ModuleFactory.create_module("transport")

        self.assertTrue(isinstance(light_module, type(ctrl := Controller().lighting)))
        self.assertTrue(isinstance(transport_module, type(Controller().transport)))

    def test_builder_schedule(self):
        """Builder Pattern Test"""
        builder = TrafficBuilder()
        schedule = (builder
                    .add_route("North → South")
                    .set_peak_hours("07:00–09:00")
                    .set_light_timing(60)
                    .build())

        self.assertTrue(isinstance(schedule, TrafficSchedule))
        self.assertEqual(schedule.peak_hours, "07:00–09:00")
        self.assertEqual(schedule.light_timing, 60)
        self.assertIn("North → South", schedule.routes)

    def test_composite_lights(self):
        """Composite + Decorator Pattern Test"""
        group = LightGroup("Test District")

        l1 = BasicLight(1)
        l2 = BasicLight(2)
        decorated = LoggingDecorator(BasicLight(3))

        group.add(l1)
        group.add(l2)
        group.add(decorated)
        group.turn_on()

        self.assertTrue(l1.is_on)
        self.assertTrue(l2.is_on)

        # turn off all
        group.turn_off()
        self.assertFalse(l1.is_on)
        self.assertFalse(l2.is_on)

    def test_transport_composite(self):
        """Composite Pattern Test for Vehicle Fleets"""
        fleet = Transports("Metro Fleet")
        v1 = Vehicle(1, "Bus")
        v2 = Vehicle(2, "Tram")

        fleet.add_vehicle(v1)
        fleet.add_vehicle(v2)

        fleet.run_all()
        # We check states via last_action flag for simulation
        self.assertEqual(v1.status(), "running")
        self.assertEqual(v2.status(), "running")

        fleet.stop_all()
        self.assertEqual(v1.status(), "stopped")
        self.assertEqual(v2.status(), "stopped")

    def test_weather_adapter(self):
        """Adapter Pattern Test"""
        provider = WeatherProvider()
        adapter = WeatherAdapter(provider)
        info = adapter.get_weather()

        self.assertTrue(hasattr(info, "condition"))
        self.assertTrue(hasattr(info, "temperature"))
        self.assertEqual(info.condition, "Sunny")
        self.assertEqual(info.temperature, 26.5)


if __name__ == "__main__":
    unittest.main()
