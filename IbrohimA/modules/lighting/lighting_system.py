"""
Lighting subsystem - Main subsystem manager
"""

from core.factories.factories import ISubsystem
from typing import Dict


class LightingSystem(ISubsystem):
    """
    Lighting Subsystem - Manages all lighting devices in the city
    """
    
    def __init__(self):
        self.name = "Lighting System"
        self.devices: Dict[str, any] = {}
        self.is_running = False
    
    def get_name(self) -> str:
        return self.name
    
    def initialize(self):
        """Initialize lighting system"""
        self.is_running = True
        print(f"✓ {self.name} initialized")
    
    def shutdown(self):
        """Shutdown lighting system"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
        self.is_running = False
        print(f"✗ {self.name} shut down")
    
    def add_device(self, device_id: str, device):
        """Add a lighting device"""
        self.devices[device_id] = device
        print(f"[LIGHTING] Added device: {device_id}")
    
    def get_status(self) -> dict:
        """Get status of all lighting devices"""
        devices_status = {}
        for device_id, device in self.devices.items():
            if hasattr(device, 'status'):
                devices_status[device_id] = device.status()
        
        return {
            'system_name': self.name,
            'is_running': self.is_running,
            'device_count': len(self.devices),
            'devices': devices_status
        }
    
    def start_all(self):
        """Start all lighting devices"""
        for device in self.devices.values():
            if hasattr(device, 'start'):
                device.start()
    
    def stop_all(self):
        """Stop all lighting devices"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
