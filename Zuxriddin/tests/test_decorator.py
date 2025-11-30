import unittest
from unittest.mock import patch
from modules.energy.meters import SmartEnergyMeter, EnergyMeter

class TestDecorator(unittest.TestCase):
    def test_decorator_wraps_component(self):
        base_meter = EnergyMeter()
        smart_meter = SmartEnergyMeter(base_meter)
        self.assertIs(smart_meter.meter, base_meter)

    @patch('builtins.print')
    def test_decorator_adds_behavior(self, mock_print):
        base_meter = EnergyMeter()
        smart_meter = SmartEnergyMeter(base_meter)
        smart_meter.start_monitoring()
        mock_print.assert_any_call("🧠 Smart Energy System: AI optimization enabled")
        mock_print.assert_any_call("⚡ Energy Meter: Monitoring started")