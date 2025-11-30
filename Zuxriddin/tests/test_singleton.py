import unittest
from core.controller import SmartCityController

class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        controller1 = SmartCityController()
        controller2 = SmartCityController()
        self.assertIs(controller1, controller2)

    def test_singleton_initialization_once(self):
        # Reset instance to test reinitialization (for test safety)
        SmartCityController._instance = None
        c1 = SmartCityController()
        c2 = SmartCityController()
        self.assertTrue(hasattr(c1, 'lighting'))
        self.assertIs(c1, c2)