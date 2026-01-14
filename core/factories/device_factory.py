"""
Device Factory - Creates various smart city devices

Design Pattern: FACTORY METHOD
Purpose: Creates different types of devices without specifying exact classes
"""

from abc import ABC, abstractmethod


class SmartDevice(ABC):
    """Abstract base class for all smart devices"""
    
    def __init__(self, device_id: str, location: str):
        self.device_id = device_id
        self.location = location
        self.is_active = False
    
    @abstractmethod
    def activate(self):
        """Activate the device"""
        pass
    
    @abstractmethod
    def deactivate(self):
        """Deactivate the device"""
        pass
    
    @abstractmethod
    def get_status(self) -> str:
        """Get device status"""
        pass


class DeviceFactory(ABC):
    """
    Factory Method Pattern
    Abstract factory for creating smart devices
    """
    
    @abstractmethod
    def create_device(self, device_id: str, location: str) -> SmartDevice:
        """Factory method to create devices"""
        pass
    
    def deploy_device(self, device_id: str, location: str) -> SmartDevice:
        """Template method using factory method"""
        device = self.create_device(device_id, location)
        print(f"✓ Deployed {device.__class__.__name__} at {location}")
        return device