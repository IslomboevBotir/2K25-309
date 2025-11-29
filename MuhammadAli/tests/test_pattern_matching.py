from smartcity.command_processor import CommandProcessor
from unittest.mock import MagicMock

def test_pattern_matching_recognizes_commands():
    ctrl = MagicMock()
    proc = CommandProcessor()

    proc.process("transport", ctrl)
    ctrl.manage_transport.assert_called_once()

    proc.process("lighting", ctrl)
    ctrl.manage_lighting.assert_called()

    proc.process("camera smart2025", ctrl)
    ctrl.access_security_camera.assert_called_with("smart2025")