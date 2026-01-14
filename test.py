import unittest
from core.controller import CityController
from core.factories.device_factory import DeviceFactory
from modules.transport.transport_system import TrafficLight, PublicTransport
from modules.transport.transport_manager import TrafficLightFactory, PublicTransportFactory
from modules.lighting.lighting_system import StreetLight, DimmableLight, MotionSensorLight
from modules.security.security_system import Camera, AlarmSystem, SecurityDeviceProxy
from modules.energy.energy_system import SolarPanelBuilder, WindTurbineBuilder, EnergyDirector


class TestSingletonPattern(unittest.TestCase):
    """Test Singleton Pattern - CityController"""
    
    def test_singleton_instance(self):
        """Test that only one instance exists"""
        controller1 = CityController.get_instance()
        controller2 = CityController.get_instance()
        self.assertIs(controller1, controller2)
    
    def test_singleton_state_persistence(self):
        """Test that state persists across instances"""
        controller1 = CityController.get_instance()
        controller1.set_city_name("TestCity")
        
        controller2 = CityController.get_instance()
        self.assertEqual(controller2.get_city_name(), "TestCity")


class TestFactoryPattern(unittest.TestCase):
    """Test Factory Method Pattern - Device Creation"""
    
    def test_traffic_light_factory(self):
        """Test traffic light creation"""
        factory = TrafficLightFactory()
        device = factory.create_device("TL001", "Main St")
        self.assertIsInstance(device, TrafficLight)
        self.assertEqual(device.device_id, "TL001")
        self.assertEqual(device.location, "Main St")
    
    def test_public_transport_factory(self):
        """Test public transport creation"""
        factory = PublicTransportFactory()
        device = factory.create_device("PT001", "Route 42")
        self.assertIsInstance(device, PublicTransport)
        self.assertEqual(device.route, "Route 42")
    
    def test_traffic_light_states(self):
        """Test traffic light state changes"""
        factory = TrafficLightFactory()
        light = factory.create_device("TL002", "Park Ave")
        light.activate()
        
        light.set_state("green")
        self.assertEqual(light.current_state, "green")
        
        light.set_state("red")
        self.assertEqual(light.current_state, "red")


class TestDecoratorPattern(unittest.TestCase):
    """Test Decorator Pattern - Lighting System"""
    
    def test_basic_light(self):
        """Test basic light functionality"""
        light = StreetLight("Main St")
        light.turn_on()
        self.assertTrue(light.is_on)
        self.assertEqual(light.get_brightness(), 100)
    
    def test_dimmable_decorator(self):
        """Test dimmable light decorator"""
        light = StreetLight("Main St")
        dimmable = DimmableLight(light)
        
        dimmable.turn_on()
        dimmable.set_brightness(50)
        self.assertEqual(dimmable.get_brightness(), 50)
    
    def test_motion_sensor_decorator(self):
        """Test motion sensor decorator"""
        light = StreetLight("Park St")
        motion_light = MotionSensorLight(light)
        
        motion_light.detect_motion()
        self.assertTrue(motion_light.motion_detected)
    
    def test_multiple_decorators(self):
        """Test stacking multiple decorators"""
        light = StreetLight("Downtown")
        dimmable = DimmableLight(light)
        motion_dimmable = MotionSensorLight(dimmable)
        
        self.assertIn("Motion Sensor", motion_dimmable.get_description())
        self.assertIn("Dimmable", motion_dimmable.get_description())


class TestProxyPattern(unittest.TestCase):
    """Test Proxy Pattern - Security System"""
    
    def test_camera_direct_access(self):
        """Test direct camera access"""
        camera = Camera("Bank")
        camera.activate()
        self.assertTrue(camera.is_recording)
    
    def test_proxy_admin_access(self):
        """Test proxy with admin access"""
        camera = Camera("Bank")
        proxy = SecurityDeviceProxy(camera, "admin")
        proxy.activate()
        self.assertTrue(camera.is_recording)
    
    def test_proxy_guest_access_denied(self):
        """Test proxy denies guest access"""
        camera = Camera("Bank")
        proxy = SecurityDeviceProxy(camera, "guest")
        proxy.activate()
        self.assertFalse(camera.is_recording)
    
    def test_proxy_access_logging(self):
        """Test proxy logs access attempts"""
        alarm = AlarmSystem("Museum")
        proxy = SecurityDeviceProxy(alarm, "admin")
        proxy.activate()
        
        log = proxy.get_access_log()
        self.assertTrue(len(log) > 0)
        self.assertIn("ACTIVATE", log[0])


class TestBuilderPattern(unittest.TestCase):
    """Test Builder Pattern - Energy System"""
    
    def test_solar_panel_builder(self):
        """Test solar panel construction"""
        builder = SolarPanelBuilder()
        director = EnergyDirector(builder)
        
        solar = director.construct_basic_solar("Roof A")
        self.assertEqual(solar.location, "Roof A")
        self.assertEqual(solar.capacity, 100)
        self.assertGreater(len(solar.components), 0)
    
    def test_wind_turbine_builder(self):
        """Test wind turbine construction"""
        builder = WindTurbineBuilder()
        director = EnergyDirector(builder)
        
        wind = director.construct_advanced_wind("Hill B")
        self.assertEqual(wind.location, "Hill B")
        self.assertEqual(wind.capacity, 800)
        self.assertIn("Gearbox", wind.components)
    
    def test_builder_chaining(self):
        """Test builder method chaining"""
        builder = SolarPanelBuilder()
        source = (builder
                  .create_source()
                  .set_location("Test")
                  .set_capacity(200)
                  .set_efficiency(0.9)
                  .build())
        
        self.assertEqual(source.location, "Test")
        self.assertEqual(source.capacity, 200)
        self.assertEqual(source.efficiency, 0.9)


class TestFacadePattern(unittest.TestCase):
    """Test Facade Pattern - City Controller"""
    
    def setUp(self):
        """Set up test controller"""
        self.controller = CityController.get_instance()
    
    def test_facade_traffic_management(self):
        """Test traffic management through facade"""
        self.controller.manage_traffic("Test St", "green")
        # Should not raise exception
        self.assertTrue(True)
    
    def test_facade_lighting_control(self):
        """Test lighting control through facade"""
        self.controller.control_lighting("Test Zone", "on", 100)
        # Should not raise exception
        self.assertTrue(True)
    
    def test_facade_security_monitoring(self):
        """Test security monitoring through facade"""
        self.controller.monitor_security("Test Location", "camera")
        # Should not raise exception
        self.assertTrue(True)
    
    def test_facade_energy_management(self):
        """Test energy management through facade"""
        self.controller.manage_energy("Test Farm", "solar")
        # Should not raise exception
        self.assertTrue(True)
    
    def test_facade_report_generation(self):
        """Test report generation"""
        report = self.controller.generate_report()
        self.assertIsInstance(report, str)
        self.assertIn("SMART CITY REPORT", report)


class TestIntegration(unittest.TestCase):
    """Integration tests for the entire system"""
    
    def test_complete_workflow(self):
        """Test complete system workflow"""
        controller = CityController.get_instance()
        
        # Set up city
        controller.set_city_name("TestCity")
        
        # Add traffic management
        controller.manage_traffic("Main & 1st", "green")
        
        # Add lighting
        controller.control_lighting("Downtown", "on", 80)
        
        # Add security
        controller.monitor_security("City Hall", "camera")
        
        # Add energy
        controller.manage_energy("Solar Farm", "solar")
        
        # Generate report
        report = controller.generate_report()
        
        self.assertIn("TestCity", report)
        self.assertIsInstance(report, str)
    
    def test_system_status(self):
        """Test system status reporting"""
        controller = CityController.get_instance()
        status = controller.get_status()
        self.assertIsInstance(status, str)


def run_tests():
    """Run all tests with detailed output"""
    print("=" * 70)
    print("🧪 SMARTCITY SYSTEM - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestSingletonPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestFactoryPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestDecoratorPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestProxyPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestBuilderPattern))
    suite.addTests(loader.loadTestsFromTestCase(TestFacadePattern))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print()
    print("=" * 70)
    print("📊 TEST SUMMARY")
    print("=" * 70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)