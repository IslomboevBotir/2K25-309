from core.singleton.registry import ServiceRegistry
from core.proxy.security_proxy import SecurityProxy
from typing import Optional


class SmartCityController:
    _instance: Optional["SmartCityController"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartCityController, cls).__new__(cls)
            cls._instance.registry = ServiceRegistry()
            cls._instance._security_proxy: Optional[SecurityProxy] = None
        return cls._instance

    def attach_city(self, city) -> None:
        self.registry.register("city", city)
        # attach proxy for security
        self._security_proxy = SecurityProxy(city.security)

    def status(self) -> str:
        city = self.registry.get("city")
        if not city:
            return "No city loaded."
        return (
            f"[{city.name}] Ready: transport, lighting, security, energy"
            + (", weather" if city.weather else "")
        )

    def dispatch_transport(self) -> str:
        city = self.registry.get("city")
        return city.transport.dispatch()

    def lights_on(self) -> str:
        city = self.registry.get("city")
        return city.lighting.turn_on_all()

    def lights_off(self) -> str:
        city = self.registry.get("city")
        return city.lighting.turn_off_all()

    def security_monitor(self, role: str) -> str:
        if not self._security_proxy:
            return "Security not initialized."
        return self._security_proxy.monitor(role=role)

    def energy_report(self) -> str:
        city = self.registry.get("city")
        return city.energy.report()

    def weather(self, zone: str) -> str:
        city = self.registry.get("city")
        if city.weather:
            return city.weather.get_weather_summary(zone)
        return "Weather service not configured."
