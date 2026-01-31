"""
Abstract Factory Naqshi Implementatsiyasi
Foydalanish: Bog'langan ob'ektlar oilasini yaratish (turli subsistema implementatsiyalari)
"""

from abc import ABC, abstractmethod
from typing import Protocol


class IQurilma(Protocol):
    """Barcha aqlli qurilmalar uchun interfeys"""
    def start(self): ...
    def stop(self): ...
    def status(self) -> dict: ...


class ISubsistema(ABC):
    """Barcha subsistemalar uchun interfeys"""
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def shutdown(self):
        pass
    
    @abstractmethod
    def get_status(self) -> dict:
        pass


class AqliQurilmaFabriki(ABC):
    """
    Abstract Factory - Bog'langan ob'ektlar oilasini yaratadi.
    Turli qurilma oilalarini yaratishning interfeysi.
    """
    
    @abstractmethod
    def create_device(self, device_id: str, location: str) -> IQurilma:
        pass
    
    @abstractmethod
    def get_factory_name(self) -> str:
        pass


class YoritishQurilmaFabriki(AqliQurilmaFabriki):
    """Yoritish qurilmalarini yaratish uchun konkret fabric"""
    
    def create_device(self, device_id: str, location: str):
        from modules.lighting.lighting_devices import SmartLight
        return SmartLight(device_id, location)
    
    def get_factory_name(self) -> str:
        return "Yoritish Qurilma Fabriki"


class XavfsizlikQurilmaFabriki(AqliQurilmaFabriki):
    """Xavfsizlik qurilmalarini yaratish uchun konkret fabric"""
    
    def create_device(self, device_id: str, location: str):
        from modules.security.security_devices import SecurityCamera
        return SecurityCamera(device_id, location)
    
    def get_factory_name(self) -> str:
        return "Xavfsizlik Qurilma Fabriki"


class TransportQurilmaFabriki(AqliQurilmaFabriki):
    """Transport qurilmalarini yaratish uchun konkret fabric"""
    
    def create_device(self, device_id: str, location: str):
        from modules.transport.transport_devices import TrafficLight
        return TrafficLight(device_id, location)
    
    def get_factory_name(self) -> str:
        return "Transport Qurilma Fabriki"


class EnergiyaQurilmaFabriki(AqliQurilmaFabriki):
    """Energiya qurilmalarini yaratish uchun konkret fabric"""
    
    def create_device(self, device_id: str, location: str):
        from modules.energy.energy_devices import EnergyMonitor
        return EnergyMonitor(device_id, location)
    
    def get_factory_name(self) -> str:
        return "Energiya Qurilma Fabriki"


# Ingliz tilidagi nomlar ham qamralib, eski kod uchun
ISubsystem = ISubsistema
SmartDeviceFactory = AqliQurilmaFabriki
LightingDeviceFactory = YoritishQurilmaFabriki
SecurityDeviceFactory = XavfsizlikQurilmaFabriki
TransportDeviceFactory = TransportQurilmaFabriki
EnergyDeviceFactory = EnergiyaQurilmaFabriki
