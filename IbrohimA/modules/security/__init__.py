"""
Security subsystem - Main subsystem manager
"""

from core.factories.factories import ISubsystem
from typing import Dict


class SecuritySystem(ISubsystem):
    """
    Security Subsystem - Manages all security devices in the city
    """
    
    def __init__(self):
        self.name = "Security System"
        self.devices: Dict[str, any] = {}
        self.is_running = False
        self.alert_level = "normal"
    
    def get_name(self) -> str:
        return self.name
    
    def initialize(self):
        """Initialize security system"""
        self.is_running = True
        print(f"✓ {self.name} initialized")
    
    def shutdown(self):
        """Shutdown security system"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
        self.is_running = False
        print(f"✗ {self.name} shut down")
    
    def add_device(self, device_id: str, device):
        """Add a security device"""
        self.devices[device_id] = device
        print(f"[SECURITY] Added device: {device_id}")
    
    def get_status(self) -> dict:
        """Get status of all security devices"""
        devices_status = {}
        for device_id, device in self.devices.items():
            if hasattr(device, 'status'):
                devices_status[device_id] = device.status()
        
        return {
            'system_name': self.name,
            'is_running': self.is_running,
            'alert_level': self.alert_level,
            'device_count': len(self.devices),
            'devices': devices_status
        }
    
    def start_all(self):
        """Start recording on all cameras"""
        for device in self.devices.values():
            if hasattr(device, 'start'):
                device.start()
    
    def stop_all(self):
        """Stop recording on all cameras"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
    
    def set_alert_level(self, level: str):
        """Set security alert level"""
        self.alert_level = level
        print(f"[SECURITY] Alert level set to: {level}")
