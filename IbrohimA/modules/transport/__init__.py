"""
Transport subsystem - Main subsystem manager
"""

from core.factories.factories import ISubsystem
from typing import Dict


class TransportSystem(ISubsystem):
    """
    Transport Subsystem - Manages traffic lights and transportation infrastructure
    """
    
    def __init__(self):
        self.name = "Transport System"
        self.devices: Dict[str, any] = {}
        self.is_running = False
        self.traffic_flow = "normal"
    
    def get_name(self) -> str:
        return self.name
    
    def initialize(self):
        """Initialize transport system"""
        self.is_running = True
        print(f"✓ {self.name} initialized")
    
    def shutdown(self):
        """Shutdown transport system"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
        self.is_running = False
        print(f"✗ {self.name} shut down")
    
    def add_device(self, device_id: str, device):
        """Add a transport device"""
        self.devices[device_id] = device
        print(f"[TRANSPORT] Added device: {device_id}")
    
    def get_status(self) -> dict:
        """Get status of all transport devices"""
        devices_status = {}
        for device_id, device in self.devices.items():
            if hasattr(device, 'status'):
                devices_status[device_id] = device.status()
        
        return {
            'system_name': self.name,
            'is_running': self.is_running,
            'traffic_flow': self.traffic_flow,
            'device_count': len(self.devices),
            'devices': devices_status
        }
    
    def start_all(self):
        """Start all traffic lights"""
        for device in self.devices.values():
            if hasattr(device, 'start'):
                device.start()
    
    def stop_all(self):
        """Stop all traffic lights"""
        for device in self.devices.values():
            if hasattr(device, 'stop'):
                device.stop()
    
    def optimize_traffic_flow(self):
        """Optimize traffic flow"""
        self.traffic_flow = "optimized"
        print(f"[TRANSPORT] Traffic flow optimized")
