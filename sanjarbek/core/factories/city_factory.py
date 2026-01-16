# core/factories/city_factory.py

from abc import ABC, abstractmethod

from modules.transport.transport import TransportSystem
from modules.lighting.lighting import LightingSystem
from modules.energy.energy import EnergySystem
from modules.security.security import SecuritySystem


class CityFactory(ABC):
    """
    Pattern: Abstract Factory (Yaratish)

    Maqsad:
    Shahar kichik tizimlarini (transport, yoritish, energiya, xavfsizlik) yaratish uchun yagona interfeys.
    Controller (boshqaruvchi) faqat shu interfeysga tayanadi, shuning uchun turli konfiguratsiyalarni (Oddiy/Premium) oson almashtirish mumkin:
    - BasicCityFactory
    - PremiumCityFactory
    """

    @abstractmethod
    def create_transport(self) -> TransportSystem:
        raise NotImplementedError

    @abstractmethod
    def create_lighting(self) -> LightingSystem:
        raise NotImplementedError

    @abstractmethod
    def create_energy(self) -> EnergySystem:
        raise NotImplementedError

    @abstractmethod
    def create_security(self) -> SecuritySystem:
        raise NotImplementedError


class BasicCityFactory(CityFactory):
    """
    Oddiy konfiguratsiya: kamroq zona, kamroq avtobus, o‘rtacha xavfsizlik, pastroq energiya sarfi.
    """

    def create_transport(self) -> TransportSystem:
        return TransportSystem(max_buses=10)

    def create_lighting(self) -> LightingSystem:
        return LightingSystem(zone_count=3)

    def create_energy(self) -> EnergySystem:
        return EnergySystem(base_consumption_kw=120)

    def create_security(self) -> SecuritySystem:
        return SecuritySystem(sensitivity="medium")


class PremiumCityFactory(CityFactory):
    """
    Premium configuration: more zones, more buses, high security, higher consumption.
    """

    def create_transport(self) -> TransportSystem:
        return TransportSystem(max_buses=25)

    def create_lighting(self) -> LightingSystem:
        return LightingSystem(zone_count=8)

    def create_energy(self) -> EnergySystem:
        return EnergySystem(base_consumption_kw=300)

    def create_security(self) -> SecuritySystem:
        return SecuritySystem(sensitivity="high")
