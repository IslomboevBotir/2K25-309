import unittest
from unittest.mock import patch
from core.controller import SmartCityController

class TestFacade(unittest.TestCase):
    @patch('modules.lighting.lighting_factory.LightingSystemFactory.create_system')
    @patch('modules.transport.transport_factory.TransportSystemFactory.create_system')
    def test_facade_initializes_subsystems(self, mock_transport, mock_lighting):
        SmartCityController._instance = None  # Reset singleton
        controller = SmartCityController()
        mock_lighting.assert_called_once()
        mock_transport.assert_called_once()

    @patch('builtins.print')
    def test_start_city_calls_all_subsystems(self, mock_print):
        SmartCityController._instance = None
        controller = SmartCityController()

        with patch.multiple(controller,
                            lighting=unittest.mock.MagicMock(),
                            transport=unittest.mock.MagicMock(),
                            security=unittest.mock.MagicMock(),
                            energy=unittest.mock.MagicMock()):
            controller.start_city()
            controller.lighting.turn_on.assert_called_once()
            controller.transport.start_service.assert_called_once()
            controller.security.activate.assert_called_once()
            controller.energy.start_monitoring.assert_called_once()