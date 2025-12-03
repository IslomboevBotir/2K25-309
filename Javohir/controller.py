from builder import SmartCityBuilder
from logger import Logger
from adapter import WeatherAdapter, ExternalWeatherAPI

class SystemController:
    _instance = None

    def __init__(self):
        if SystemController._instance is not None:
            raise Exception("Singleton!")
        self.log = Logger.get_instance()
        self.city = SmartCityBuilder()\
            .add_lighting()\
            .add_transport()\
            .add_security()\
            .add_energy()\
            .build()
        self.weather = WeatherAdapter()
        self.log.log("SmartCityController ishga tushdi!")

    @staticmethod
    def get_instance():
        if SystemController._instance is None:
            SystemController._instance = SystemController()
        return SystemController._instance

    def start_city(self):
        print("=== SHAHAR TIZIMLARI ISHGA TUSHIRILDI ===")
        self.city["lighting"].turn_on()
        self.city["transport"].show_routes()
        self.city["security"].scan()
