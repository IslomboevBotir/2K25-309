"""
SmartCity Tizimi uchun Unit Testlar
Barcha dizayn naqshlari va asosiy funksionallikni test qiladi
"""

import unittest
import sys
import os

# Loyiha ildizini path ga qo'shish
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.controller import SmartCityController
from core.singelton.singleton import Singleton
from core.builders.builders import SmartCityBuilder, SmartCityBiluvchi
from core.factories.factories import (
    YoritishQurilmaFabriki,
    XavfsizlikQurilmaFabriki,
    TransportQurilmaFabriki,
    EnergiyaQurilmaFabriki,
    LightingDeviceFactory,
    SecurityDeviceFactory,
    TransportDeviceFactory,
    EnergyDeviceFactory
)
from core.proxy.proxy import SubsistemProxy, SubsystemProxy
from core.adapters.adapters import (
    MonitoringDekorator,
    SecurityDekorator,
    LoggingDekorator,
    MonitoringDecorator,
    SecurityDecorator,
    LoggingDecorator
)
from modules.lighting.lighting_system import LightingSystem
from modules.lighting.lighting_devices import SmartLight
from modules.security.security_devices import SecurityCamera
from modules.transport.transport_devices import TrafficLight
from modules.energy.energy_devices import EnergyMonitor


class TestSingletonPattern(unittest.TestCase):
    """Test Singleton Pattern"""
    
    def test_controller_singleton(self):
        """Test that controller is a singleton"""
        # Create multiple instances
        controller1 = SmartCityController()
        controller2 = SmartCityController()
        
        # Should be the same instance
        self.assertIs(controller1, controller2)
        print("✓ Singleton Pattern: Multiple instances are the same")
    
    def test_singleton_identity(self):
        """Test singleton identity"""
        ctrl1 = SmartCityController()
        ctrl2 = SmartCityController()
        self.assertEqual(id(ctrl1), id(ctrl2))
        print("✓ Singleton Pattern: ID verification passed")


class TestFactoryPattern(unittest.TestCase):
    """Test Abstract Factory and Factory Method Patterns"""
    
    def test_lighting_factory(self):
        """Test lighting device factory"""
        factory = LightingDeviceFactory()
        device = factory.create_device("LIGHT-001", "Main Street")
        self.assertIsInstance(device, SmartLight)
        self.assertEqual(device.device_id, "LIGHT-001")
        print("✓ Factory Pattern: Lighting factory creates correct device")
    
    def test_security_factory(self):
        """Test security device factory"""
        factory = SecurityDeviceFactory()
        device = factory.create_device("CAM-001", "Downtown")
        self.assertIsInstance(device, SecurityCamera)
        self.assertEqual(device.device_id, "CAM-001")
        print("✓ Factory Pattern: Security factory creates correct device")
    
    def test_transport_factory(self):
        """Test transport device factory"""
        factory = TransportDeviceFactory()
        device = factory.create_device("TRAFFIC-001", "Main Intersection")
        self.assertIsInstance(device, TrafficLight)
        print("✓ Factory Pattern: Transport factory creates correct device")
    
    def test_energy_factory(self):
        """Test energy device factory"""
        factory = EnergyDeviceFactory()
        device = factory.create_device("ENERGY-001", "Zone-1")
        self.assertIsInstance(device, EnergyMonitor)
        print("✓ Factory Pattern: Energy factory creates correct device")


class TestBuilderPattern(unittest.TestCase):
    """Test Builder Pattern"""
    
    def test_basic_builder(self):
        """Test basic configuration building"""
        builder = SmartCityBuilder("TestCity")
        config = builder.build()
        self.assertEqual(config.city_name, "TestCity")
        print("✓ Builder Pattern: Basic city configuration created")
    
    def test_builder_chaining(self):
        """Test builder method chaining"""
        config = (SmartCityBuilder("SmartTestCity")
                 .add_lighting_system(5)
                 .add_security_system(3)
                 .add_transport_system(4)
                 .add_energy_system(2)
                 .set_auto_start(True)
                 .build())
        
        self.assertEqual(config.num_lighting_devices, 5)
        self.assertEqual(config.num_security_cameras, 3)
        self.assertEqual(config.num_traffic_lights, 4)
        self.assertEqual(config.num_energy_monitors, 2)
        self.assertTrue(config.auto_start)
        print("✓ Builder Pattern: Complete configuration with method chaining")
    
    def test_builder_custom_locations(self):
        """Test builder with custom locations"""
        locations = ["Street A", "Street B", "Street C"]
        config = (SmartCityBuilder("TestCity")
                 .add_lighting_system(3, locations)
                 .build())
        
        self.assertEqual(config.device_configs['lighting']['locations'], locations)
        print("✓ Builder Pattern: Custom locations configuration")


class TestProxyPattern(unittest.TestCase):
    """Test Proxy Pattern"""
    
    def test_proxy_lazy_initialization(self):
        """Test proxy lazy initialization"""
        system = LightingSystem()
        proxy = SubsystemProxy(system)
        
        # Not initialized yet
        self.assertFalse(proxy._initialized)
        
        # Access through proxy should initialize
        proxy.get_status()
        self.assertTrue(proxy._initialized)
        print("✓ Proxy Pattern: Lazy initialization works")
    
    def test_proxy_access_control(self):
        """Test proxy access control"""
        system = LightingSystem()
        proxy = SubsystemProxy(system)
        
        # Allowed command
        result = proxy.execute_command("start")
        self.assertTrue(result)
        
        # Disallowed command
        result = proxy.execute_command("invalid_command")
        self.assertFalse(result)
        print("✓ Proxy Pattern: Access control working")
    
    def test_proxy_access_count(self):
        """Test proxy tracks access count"""
        system = LightingSystem()
        proxy = SubsystemProxy(system)
        
        proxy.get_status()
        status1 = proxy.get_status()
        self.assertEqual(status1['access_count'], 2)
        print("✓ Proxy Pattern: Access counting working")


class TestDecoratorPattern(unittest.TestCase):
    """Test Decorator Pattern"""
    
    def test_monitoring_decorator(self):
        """Test monitoring decorator"""
        system = LightingSystem()
        decorated = MonitoringDecorator(system)
        
        status = decorated.get_status()
        self.assertTrue(status['monitoring_enabled'])
        self.assertEqual(status['event_count'], 0)
        
        decorated.record_event("test_event")
        status = decorated.get_status()
        self.assertEqual(status['event_count'], 1)
        print("✓ Decorator Pattern: Monitoring decorator working")
    
    def test_security_decorator(self):
        """Test security decorator"""
        system = LightingSystem()
        decorated = SecurityDecorator(system, auth_level="admin")
        
        status = decorated.get_status()
        self.assertEqual(status['security_auth_level'], "admin")
        
        decorated.lock()
        status = decorated.get_status()
        self.assertTrue(status['is_locked'])
        print("✓ Decorator Pattern: Security decorator working")
    
    def test_logging_decorator(self):
        """Test logging decorator"""
        system = LightingSystem()
        decorated = LoggingDecorator(system)
        
        decorated.add_log("Test log message")
        status = decorated.get_status()
        self.assertEqual(status['log_count'], 1)
        print("✓ Decorator Pattern: Logging decorator working")
    
    def test_stacked_decorators(self):
        """Test multiple decorators stacked"""
        system = LightingSystem()
        system = MonitoringDecorator(system)
        system = SecurityDecorator(system)
        system = LoggingDecorator(system)
        
        status = system.get_status()
        self.assertTrue('monitoring_enabled' in str(status))
        print("✓ Decorator Pattern: Multiple stacked decorators working")


class TestControllerIntegration(unittest.TestCase):
    """Test SmartCity Controller Integration"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.controller = SmartCityController()
        # Reset state for new test
        self.controller._initialized = False
        self.controller._is_running = False
        self.controller.initialize()
    
    def test_controller_initialization(self):
        """Test controller initialization"""
        # After initialize, should be initialized and running
        self.assertTrue(self.controller._initialized)
        self.assertTrue(self.controller._is_running)
        print("✓ Controller Integration: Initialization working")
    
    def test_create_device(self):
        """Test device creation via controller"""
        device = self.controller.create_device('lighting', 'LIGHT-001', 'Main St')
        self.assertIsNotNone(device)
        self.assertEqual(device.device_id, 'LIGHT-001')
        print("✓ Controller Integration: Device creation working")
    
    def test_add_device_to_subsystem(self):
        """Test adding device to subsystem"""
        device = self.controller.create_device('lighting', 'LIGHT-002', 'Oak Ave')
        result = self.controller.add_device_to_subsystem('lighting', 'LIGHT-002', device)
        self.assertTrue(result)
        print("✓ Controller Integration: Adding device to subsystem working")
    
    def test_get_subsystem_status(self):
        """Test getting subsystem status"""
        status = self.controller.get_subsystem_status('lighting')
        self.assertIn('system_name', status)
        self.assertEqual(status['system_name'], 'Lighting System')
        print("✓ Controller Integration: Getting subsystem status working")
    
    def test_start_stop_subsystem(self):
        """Test starting and stopping subsystem"""
        # Create and add device first
        device = SmartLight('LIGHT-TEST', 'Test Street')
        self.controller.add_device_to_subsystem('lighting', 'LIGHT-TEST', device)
        
        # Start and check
        self.controller.start_subsystem('lighting')
        status = self.controller.get_subsystem_status('lighting')
        # Device should be on after start
        
        # Stop and check
        self.controller.stop_subsystem('lighting')
        print("✓ Controller Integration: Start/stop subsystem working")
    
    def tearDown(self):
        """Clean up after tests"""
        self.controller.shutdown()


class TestLightingSystem(unittest.TestCase):
    """Test Lighting System Functionality"""
    
    def test_smart_light_on_off(self):
        """Test smart light on/off"""
        light = SmartLight("LIGHT-001", "Main Street")
        
        light.start()
        self.assertTrue(light.is_on)
        self.assertEqual(light.brightness, 100)
        
        light.stop()
        self.assertFalse(light.is_on)
        self.assertEqual(light.brightness, 0)
        print("✓ Lighting System: Smart light on/off working")
    
    def test_light_brightness(self):
        """Test brightness adjustment"""
        light = SmartLight("LIGHT-002", "Oak Avenue")
        light.set_brightness(50)
        self.assertEqual(light.brightness, 50)
        
        light.set_brightness(200)  # Should cap at 100
        self.assertEqual(light.brightness, 100)
        print("✓ Lighting System: Brightness adjustment working")


class TestSecuritySystem(unittest.TestCase):
    """Test Security System Functionality"""
    
    def test_security_camera(self):
        """Test security camera"""
        camera = SecurityCamera("CAM-001", "Downtown")
        
        camera.start()
        self.assertTrue(camera.is_recording)
        
        camera.stop()
        self.assertFalse(camera.is_recording)
        print("✓ Security System: Camera on/off working")


class TestTransportSystem(unittest.TestCase):
    """Test Transport System Functionality"""
    
    def test_traffic_light_signals(self):
        """Test traffic light signal changes"""
        traffic = TrafficLight("TRAFFIC-001", "Main Intersection")
        
        traffic.start()
        self.assertTrue(traffic.is_operational)
        
        traffic.set_signal("green")
        self.assertEqual(traffic.current_signal, "green")
        
        traffic.set_signal("red")
        self.assertEqual(traffic.current_signal, "red")
        
        traffic.stop()
        self.assertFalse(traffic.is_operational)
        print("✓ Transport System: Traffic light signals working")


class TestEnergySystem(unittest.TestCase):
    """Test Energy System Functionality"""
    
    def test_energy_monitor(self):
        """Test energy monitoring"""
        monitor = EnergyMonitor("ENERGY-001", "Zone-1")
        
        monitor.start()
        self.assertTrue(monitor.is_monitoring)
        
        monitor.update_consumption(45.5)
        self.assertEqual(monitor.power_consumption, 45.5)
        
        monitor.stop()
        self.assertFalse(monitor.is_monitoring)
        print("✓ Energy System: Energy monitoring working")


def run_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("RUNNING SMARTCITY SYSTEM UNIT TESTS")
    print("="*60 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestSingletonPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestFactoryPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestBuilderPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestProxyPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestDecoratorPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestControllerIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestLightingSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestSecuritySystem))
    suite.addTests(loader.loadTestsFromTestCase(TestTransportSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestEnergySystem))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*60 + "\n")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
