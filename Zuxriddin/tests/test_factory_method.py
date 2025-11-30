import unittest
from modules.transport.transport_factory import TransportSystemFactory
from modules.transport.vehicles import Bus, Tram

class TestFactoryMethod(unittest.TestCase):
    def test_bus_system_created(self):
        system = TransportSystemFactory.create_system("bus")
        self.assertIsInstance(system, type(TransportSystemFactory.create_system("bus")))

    def test_tram_system_created(self):
        system = TransportSystemFactory.create_system("tram")
        self.assertIsInstance(system, type(TransportSystemFactory.create_system("tram")))

    @unittest.mock.patch('builtins.print')
    def test_bus_start_prints_message(self, mock_print):
        system = TransportSystemFactory.create_system("bus")
        system.start_service()
        mock_print.assert_called_with("🚌 City Bus: Service started")