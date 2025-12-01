from core.singleton.logger import Logger
from core.factories.device_factory import EnergySavingFactory
from core.adapters.weather_adapter import WeatherAdapter, ExternalWeatherService
from core.proxy.security_proxy import SecurityProxy
from modules.lighting.lighting import LightingSubsystem
from modules.transport.transport import TransportSubsystem
from modules.energy.energy import EnergySubsystem

class SmartCityController:
    _instance = None

    def __init__(self):
        if SmartCityController._instance is not None:
            raise Exception('Use get_instance()')
        self.logger = Logger.get_instance()
        self.factory = EnergySavingFactory()
        self.lighting = LightingSubsystem(self.factory)
        self.transport = TransportSubsystem(self.factory)
        self.energy = EnergySubsystem()
        self.security_proxy = SecurityProxy(user_role='guest')
        self.weather_adapter = WeatherAdapter(ExternalWeatherService())

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = SmartCityController()
        return cls._instance

    def bootstrap(self):
        self.logger.log('SmartCityController bootstrap')

    def status(self):
        print('--- SmartCity Status ---')
        self.lighting.status()
        self.transport.generate_report()
        self.energy.generate_report()

    def fetch_weather(self):
        w = self.weather_adapter.current_weather()
        print(f"Weather: {w['condition']}, {w['temperature_celsius']} C")
