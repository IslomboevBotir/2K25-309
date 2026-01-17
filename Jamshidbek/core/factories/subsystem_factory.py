from Jamshidbek.core.adapters.weather_adapter import ExternalWeatherService, WeatherAdapter
from Jamshidbek.core.proxy.security_proxy import SecurityProxy
from Jamshidbek.modules.energy.energy import EnergySystem
from Jamshidbek.modules.lighting.lighting import LightingSystem, EcoLightingDecorator
from Jamshidbek.modules.security.security import SecuritySystem
from Jamshidbek.modules.transport.transport import TransportSystem


class SmartCityAbstractFactory:
    """
    Abstract Factory Pattern:
    Creates related subsystems consistently.
    """
    def create_lighting(self): raise NotImplementedError
    def create_transport(self): raise NotImplementedError
    def create_security(self): raise NotImplementedError
    def create_energy(self): raise NotImplementedError
    def create_weather(self): raise NotImplementedError


class DefaultCityFactory(SmartCityAbstractFactory):
    def __init__(self, city_name: str, eco_mode: bool, role: str) -> None:
        self.city_name = city_name
        self.eco_mode = eco_mode
        self.role = role if role in ("admin", "guest") else "guest"

    def create_lighting(self):
        base = LightingSystem()
        if self.eco_mode:
            return EcoLightingDecorator(base, max_brightness=60)
        return base

    def create_transport(self):
        return TransportSystem()

    def create_security(self):
        return SecurityProxy(SecuritySystem(), role=self.role)

    def create_energy(self):
        return EnergySystem()

    def create_weather(self):
        return WeatherAdapter(ExternalWeatherService(), city=self.city_name)
