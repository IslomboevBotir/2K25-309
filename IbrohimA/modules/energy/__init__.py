"""
Energy subsystem - Main subsystem manager
"""

from core.factories.factories import ISubsystem
from typing import Dict


class EnergySystem(ISubsystem):
    """
    Energy Subsystem - Manages energy monitoring and optimization
    """
    
    def __init__(self):
        self.name = "Energy System"
        self.devices: Dict[str, any] = {}
        self.is_running = False
        self.total_consumption = 0.0  # kWh
        self.efficiency_mode = False
    
    def get_name(self) -> str:
        return self.name
    
    def initialize(self):
        """Initialize energy system"""
        self.is_running = True
        print(f"✓ {self.name} initialized")
    
    def shutdown(self):
        """Shutdown energy system"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
        self.is_running = False
        print(f"✗ {self.name} shut down")
    
    def add_device(self, device_id: str, device):
        """Add an energy device"""
        self.devices[device_id] = device
        print(f"[ENERGY] Added device: {device_id}")
    
    def get_status(self) -> dict:
        """Get status of all energy devices"""
        devices_status = {}
        for device_id, device in self.devices.items():
            if hasattr(device, 'status'):
                devices_status[device_id] = device.status()
        
        return {
            'system_name': self.name,
            'is_running': self.is_running,
            'efficiency_mode': self.efficiency_mode,
            'total_consumption_kwh': self.total_consumption,
            'device_count': len(self.devices),
            'devices': devices_status
        }
    
    def start_all(self):
        """Start monitoring on all devices"""
        for device in self.devices.values():
            if hasattr(device, 'start'):
                device.start()
    
    def stop_all(self):
        """Stop monitoring on all devices"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
    
    def enable_efficiency_mode(self):
        """Enable energy efficiency mode"""
        self.efficiency_mode = True
        print(f"[ENERGY] Efficiency mode ENABLED")
    
    def calculate_total_consumption(self) -> float:
        """Calculate total consumption from all devices"""
        total = 0.0
        for device in self.devices.values():
            if hasattr(device, 'power_consumption'):
                total += device.power_consumption
        self.total_consumption = total
        return total
