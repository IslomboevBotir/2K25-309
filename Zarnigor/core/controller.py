"""
SmartCityController
- Acts as a Facade to all subsystems (Transport, Lighting, Security, Energy).
- Implemented as a Singleton to ensure only one central controller exists.
"""

from core.factories.factory import SubsystemFactory
from core.builders.builder import CityReportDirector, CityReportBuilder
from core.adapters.adapter import WeatherServiceAdapter
from core.proxy.proxy import SecurityProxy, LightingProxy
from core.singleton.logger import Logger


class SmartCityController:
    """
    Facade + Singleton.

    This class hides the complexity of subsystem initialization and
    provides a simple API for the console UI.
    """
    _instance = None  # Singleton instance storage

    def __new__(cls, *args, **kwargs):
        # Singleton pattern: create instance only once
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Protect from reinitialization in Singleton
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        self.logger = Logger()
        self.factory = SubsystemFactory()

        # Subsystems created via Abstract Factory
        self.transport = self.factory.create_transport_system()
        self.lighting = self.factory.create_lighting_system()
        self.security = self.factory.create_security_system()
        self.energy = self.factory.create_energy_system()

        # Adapter for external weather API
        self.weather_service = WeatherServiceAdapter()

        # Proxies for security and lighting subsystems
        self.security_proxy = SecurityProxy(self.security)
        self.lighting_proxy = LightingProxy(self.lighting)

        self.logger.log("SmartCityController initialized.")

    # ---------- High-level facade operations ----------

    def show_full_status(self):
        """
        Shows a combined status of transport, lighting, security and energy.
        """
        print("\n========== 📊 SMARTCITY STATUS OVERVIEW ==========")
        print(self.transport.get_status())
        print(self.lighting.get_status())
        print(self.security.get_status())
        self.energy.monitor()  # update usage
        print(self.energy.get_status())
        print("==================================================")

    def show_transport_status(self):
        msg = self.transport.get_status()
        self.logger.log(msg)
        # print(msg)

    def show_lighting_status(self):
        msg = self.lighting.get_status()
        self.logger.log(msg)
        # print(msg)

    def turn_city_lights_on(self, role: str):
        self.logger.log(f"Request: turn all lights ON by role={role}")
        self.lighting_proxy.turn_all_on(role)

    def turn_city_lights_off(self, role: str):
        self.logger.log(f"Request: turn all lights OFF by role={role}")
        self.lighting_proxy.turn_all_off(role)

    def start_traffic(self):
        """
        Starts/reports transport activity.
        """
        msg = self.transport.start_system()
        self.logger.log(msg)
        # print(msg)

    def show_security_status(self):
        self.security.status()
        self.logger.log(self.security.get_status())

    def trigger_security_alarm(self, threat: str):
        self.security.trigger_alarm(threat)
        self.logger.log(f"Security alarm triggered: {threat}")

    def reset_security_alarm(self):
        self.security.reset_alarm()
        self.logger.log("Security alarm reset.")

    def monitor_energy(self):
        self.energy.monitor()
        self.energy.status()
        self.logger.log("Energy monitored and status shown.")

    def enable_energy_optimization(self):
        self.energy.optimize()
        self.logger.log("Energy optimization enabled.")

    def disable_energy_optimization(self):
        self.energy.disable_optimization()
        self.logger.log("Energy optimization disabled.")

    def show_energy_status(self):
        self.energy.status()
        self.logger.log(self.energy.get_status())

    def generate_city_report(self) -> str:
        """
        Uses Builder pattern to generate a multi-section city report.
        """
        builder = CityReportBuilder()
        director = CityReportDirector(builder)

        director.build_full_report(
            transport_status=self.transport.get_status(),
            lighting_status=self.lighting.get_status(),
            security_status=self.security.get_status(),
            energy_status=self.energy.get_status(),
        )
        report = builder.get_result()
        self.logger.log("City report generated.")
        return report

    def show_weather(self):
        """
        Uses Adapter pattern to gather weather data from an external-like API.
        """
        info = self.weather_service.get_weather_info()
        self.logger.log(f"Weather: {info}")
        print(f"\n🌦 Current weather: {info}\n")

    def access_security(self, role: str):
        """
        Uses Proxy to control access to detailed security information.
        """
        msg = self.security_proxy.access(role)
        self.logger.log(msg)
        # print(msg)
