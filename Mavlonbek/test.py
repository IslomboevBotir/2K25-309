# FIO/test.py

import unittest
import sys
import os

# Add the FIO directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import components to test
from core.controller import SmartCityController
from core.singleton.singleton import Singleton
from core.factories.abstract_factory import BasicTrafficSensor, AdvancedTrafficSensor, BasicStreetLight, AdvancedStreetLight, BasicDeviceFactory, AdvancedDeviceFactory
from core.adapters.adapter import LegacySecurityCamera, SecurityCameraAdapter
from core.proxy.proxy import EnergyDataProxy
from core.builders.infrastructure_builder import SmartCityBuilder, InfrastructureDirector
from modules.transport.transport_module import Bus, Tram, Taxi, TransportModule
from modules.security.security_module import SecurityFeedDecorator

class TestDesignPatterns(unittest.TestCase):

    def test_01_singleton_and_facade(self):
        """Test Singleton pattern for SmartCityController."""
        # Reset the Singleton instance for a clean test
        if SmartCityController in Singleton._instances:
            del Singleton._instances[SmartCityController]

        controller1 = SmartCityController()
        controller2 = SmartCityController()
        
        # Check if both instances are the same object
        self.assertIs(controller1, controller2, "SmartCityController should be a Singleton.")
        
        # Check if Facade methods are callable (basic check)
        self.assertTrue(hasattr(controller1, 'start_city_operations'))
        self.assertTrue(hasattr(controller1, 'optimize_energy_usage'))

    def test_02_factory_method(self):
        """Test Factory Method pattern in TransportModule."""
        module = TransportModule()
        
        # Test creation of different products
        bus = module._factory_method("bus")
        tram = module._factory_method("tram")
        
        self.assertIsInstance(bus, Bus)
        self.assertIsInstance(tram, Tram)
        self.assertEqual(bus.operate(), "Bus is operating on route 101.")
        
        # Test error handling for unknown type
        with self.assertRaises(ValueError):
            module._factory_method("plane")

    def test_03_abstract_factory(self):
        """Test Abstract Factory pattern for City Devices."""
        basic_factory = BasicDeviceFactory()
        advanced_factory = AdvancedDeviceFactory()
        
        # Test Basic Factory
        basic_sensor = basic_factory.create_sensor()
        basic_actuator = basic_factory.create_actuator()
        self.assertIsInstance(basic_sensor, BasicTrafficSensor)
        self.assertIsInstance(basic_actuator, BasicStreetLight)
        
        # Test Advanced Factory
        advanced_sensor = advanced_factory.create_sensor()
        advanced_actuator = advanced_factory.create_actuator()
        self.assertIsInstance(advanced_sensor, AdvancedTrafficSensor)
        self.assertIsInstance(advanced_actuator, AdvancedStreetLight)

    def test_04_adapter(self):
        """Test Adapter pattern for LegacySecurityCamera."""
        legacy_camera = LegacySecurityCamera()
        adapter = SecurityCameraAdapter(legacy_camera)
        
        # The adapter should expose the modern interface but call the legacy method
        self.assertTrue(hasattr(adapter, 'start_feed'))
        self.assertIn("proprietary protocol", adapter.start_feed())

    def test_05_proxy(self):
        """Test Proxy pattern for EnergyDataService access control."""
        proxy = EnergyDataProxy()
        
        # Test basic data access (always allowed)
        self.assertIn("Basic Energy Data", proxy.get_basic_data())
        
        # Test sensitive data access (allowed for Admin)
        sensitive_data_admin = proxy.get_sensitive_data("Admin")
        self.assertIn("Sensitive Energy Data", sensitive_data_admin)
        
        # Test sensitive data access (denied for Citizen)
        sensitive_data_citizen = proxy.get_sensitive_data("Citizen")
        self.assertIn("Access Denied", sensitive_data_citizen)

    def test_06_builder(self):
        """Test Builder pattern for CityInfrastructure construction."""
        builder = SmartCityBuilder()
        director = InfrastructureDirector(builder)
        
        # Build full infrastructure
        director.build_full_infrastructure()
        full_infra = builder.get_result()
        self.assertIsInstance(full_infra, type(builder.get_result())) # Check if a new object is returned
        self.assertIn("Transport Network", full_infra.parts)
        self.assertIn("Smart Grid", full_infra.parts)
        self.assertIn("Security Perimeter", full_infra.parts)
        self.assertEqual(len(full_infra.parts), 3)

        # Build minimal infrastructure
        director.build_minimal_infrastructure()
        minimal_infra = builder.get_result()
        self.assertIn("Transport Network", minimal_infra.parts)
        self.assertNotIn("Smart Grid", minimal_infra.parts)
        self.assertEqual(len(minimal_infra.parts), 1)

    def test_07_decorator(self):
        """Test Decorator pattern for SecurityFeedDecorator."""
        legacy_camera = LegacySecurityCamera()
        adapter = SecurityCameraAdapter(legacy_camera)
        decorated_feed = SecurityFeedDecorator(adapter)

        result = decorated_feed.start_feed()
        # Check if the decorator added its responsibilities (Encryption and Logging)
        self.assertIn("Encrypted and Logged", result)
        self.assertIn("proprietary protocol", result) # Check if the original functionality is still present

if __name__ == '__main__':
    # The main application runs a demonstration, the test file runs unit tests.
    print("Running Unit Tests for SmartCity System Design Patterns...")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
