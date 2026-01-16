from dataclasses import dataclass
from typing import Optional
from core.factories.abstract_factory import SmartCityFactory
from core.adapters.weather_adapter import WeatherServiceAdapter


@dataclass
class City:
    name: str
    transport: any
    lighting: any
    security: any
    energy: any
    weather: Optional[WeatherServiceAdapter] = None


class CityBuilder:
    def __init__(self, factory: SmartCityFactory):
        self.factory = factory
        self._name = "SmartCity"
        self._weather: Optional[WeatherServiceAdapter] = None

    def with_name(self, name: str) -> "CityBuilder":
        self._name = name
        return self

    def with_weather(self, adapter: WeatherServiceAdapter) -> "CityBuilder":
        self._weather = adapter
        return self

    def build(self) -> City:
        transport = self.factory.create_transport()
        lighting = self.factory.create_lighting()
        security = self.factory.create_security()
        energy = self.factory.create_energy()
        return City(
            name=self._name,
            transport=transport,
            lighting=lighting,
            security=security,
            energy=energy,
            weather=self._weather,
        )
