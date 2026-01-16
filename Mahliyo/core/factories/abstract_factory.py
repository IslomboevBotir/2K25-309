from abc import ABC, abstractmethod
from typing import Protocol


class TransportSystem(Protocol):
    def add_vehicle(self, kind: str, capacity: int) -> None: 
    def dispatch(self) -> str: 


class LightingSystem(Protocol):
    def add_light(self, kind: str, power: int) -> None: 
    def turn_on_all(self) -> str: 
    def turn_off_all(self) -> str: 


class SecuritySystem(Protocol):
    def add_camera(self, resolution: str) -> None: 
    def monitor(self) -> str: 


class EnergySystem(Protocol):
    def add_meter(self, location: str) -> None: 
    def report(self) -> str: 


class SmartCityFactory(ABC):
    @abstractmethod
    def create_transport(self) -> TransportSystem: 

    @abstractmethod
    def create_lighting(self) -> LightingSystem: 

    @abstractmethod
    def create_security(self) -> SecuritySystem: 

    @abstractmethod
    def create_energy(self) -> EnergySystem: 
