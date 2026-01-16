"""
Concrete Abstract Factories and Factory Methods:
- Implements SmartCityFactory for 'EcoCity' and 'StandardCity'.
- Each subsystem exposes factory methods to create internal devices.
"""

from modules.transport.transport import TransportManager
from modules.lighting.lighting import LightingManager
from modules.security.security import SecurityManager
from modules.energy.energy import EnergyManager
from .abstract_factory import SmartCityFactory


class EcoCityFactory(SmartCityFactory):
    def create_transport(self):
        tm = TransportManager(profile="eco")
        tm.add_vehicle(kind="electric_bus", capacity=60)
        tm.add_vehicle(kind="bike", capacity=1)
        return tm

    def create_lighting(self):
        lm = LightingManager(profile="eco")
        lm.add_light(kind="led_street", power=40)
        lm.add_light(kind="solar_park", power=20)
        return lm

    def create_security(self):
        sm = SecurityManager(profile="eco")
        sm.add_camera(resolution="4K")
        return sm

    def create_energy(self):
        em = EnergyManager(profile="eco")
        em.add_meter(location="district-1")
        em.add_meter(location="district-2")
        return em


class StandardCityFactory(SmartCityFactory):
    def create_transport(self):
        tm = TransportManager(profile="standard")
        tm.add_vehicle(kind="diesel_bus", capacity=50)
        tm.add_vehicle(kind="tram", capacity=120)
        return tm

    def create_lighting(self):
        lm = LightingManager(profile="standard")
        lm.add_light(kind="halogen_street", power=100)
        lm.add_light(kind="park", power=60)
        return lm

    def create_security(self):
        sm = SecurityManager(profile="standard")
        sm.add_camera(resolution="1080p")
        sm.add_camera(resolution="720p")
        return sm

    def create_energy(self):
        em = EnergyManager(profile="standard")
        em.add_meter(location="central")
        return em
