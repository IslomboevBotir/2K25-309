"""
Unit Tests for SmartCity System
Tests all 5 design patterns
"""

import unittest
from core.controller import SmartCityController
from core.builders.city_config_builder import CityConfigBuilder
from core.factories.transport_factory import BusFactory, TramFactory
from core.factories.lighting_factory import StreetLightFactory
from core.adapters.sensor_adapter import SensorAdapter

class TestSmartCityPatterns(unittest.TestCase):
    
    def test_singleton_pattern(self):
        """Test that Singleton returns same instance"""
        controller1 = SmartCityController()
        controller2 = SmartCityController()
        self.assertIs(controller1, controller2, "Singleton should return same instance")
    
    def test_factory_method_vehicles(self):
        """Test Factory Method creates correct vehicle types"""
        bus_factory = BusFactory()
        tram_factory = TramFactory()
        
        bus = bus_factory.create_vehicle("12")
        tram = tram_factory.create_vehicle("A")
        
        self.assertIn("Bus", bus.get_status())
        self.assertIn("Tram", tram.get_status())
    
    def test_factory_method_lights(self):
        """Test Factory Method creates correct light types"""
        street_factory = StreetLightFactory()
        street_light = street_factory.create_light("Main Street")
        
        result = street_light.turn_on()
        self.assertIn("turned ON", result)
        self.assertEqual(street_light.get_brightness(), 100)
    
    def test_builder_pattern(self):
        """Test Builder creates proper configuration"""
        config = (CityConfigBuilder()
                  .set_city_name("Test City")
                  .enable_transport()
                  .enable_lighting()
                  .build())
        
        self.assertEqual(config.city_name, "Test City")
        self.assertTrue(config.transport_enabled)
        self.assertTrue(config.lighting_enabled)
    
    def test_adapter_pattern(self):
        """Test Adapter provides unified interface"""
        adapter = SensorAdapter()
        sensor_data = adapter.get_all_sensor_data()
        
        self.assertIn("weather", sensor_data)
        self.assertIn("traffic", sensor_data)
        self.assertIn("temperature", sensor_data["weather"])
        self.assertIn("vehicle_count", sensor_data["traffic"])
    
    def test_facade_pattern(self):
        """Test Facade simplifies subsystem interaction"""
        controller = SmartCityController()
        
        # Should be able to access all subsystems through facade
        self.assertIsNotNone(controller.transport)
        self.assertIsNotNone(controller.lighting)
        self.assertIsNotNone(controller.security)
        self.assertIsNotNone(controller.energy)
    
    def test_transport_system(self):
        """Test Transport subsystem functionality"""
        controller = SmartCityController()
        bus_factory = BusFactory()
        bus = bus_factory.create_vehicle("100")
        
        controller.transport.add_vehicle(bus)
        status = controller.transport.get_status()
        
        self.assertIn("Transport System", status)
    
    def test_energy_system(self):
        """Test Energy monitoring"""
        controller = SmartCityController()
        controller.energy.register_device("Test Device", 50)
        
        self.assertEqual(controller.energy.total_consumption, 50)

if __name__ == "__main__":
    print("🧪 Running SmartCity System Tests...\n")
    unittest.main(verbosity=2)