import unittest
from unittest.mock import patch
from modules.security.cameras import SecurityCameraSystem, OldCameraSystem

class TestAdapter(unittest.TestCase):
    def test_security_system_wraps_old_camera(self):
        security = SecurityCameraSystem()
        self.assertIsInstance(security.camera, OldCameraSystem)

    @patch('builtins.print')
    def test_activate_calls_old_camera_method(self, mock_print):
        security = SecurityCameraSystem()
        security.activate()
        mock_print.assert_called_with("🎥 Old Camera: Recording ON")

    def test_adapter_implements_observer_interface(self):
        security = SecurityCameraSystem()
        self.assertTrue(hasattr(security, 'update'))
        self.assertTrue(callable(getattr(security, 'update')))