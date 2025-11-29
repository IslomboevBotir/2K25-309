# smartcity/controller.py
from modules.transport import TransportSystem
from modules.lighting import LightingSystem
from modules.security import AdvancedSecuritySystem
from modules.energy import EnergySystem
from modules.weather import WeatherSystem
from modules.waste import WasteManagement
from modules.wifi import WiFiManager
from smartcity.logger import Logger

class CityController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            Logger().log("INFO", "CityController yaratilmoqda (Singleton)")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.transport = TransportSystem()
            self.lighting = LightingSystem()
            self.security = AdvancedSecuritySystem()
            self.energy = EnergySystem()
            self.weather = WeatherSystem()
            self.waste = WasteManagement()
            self.wifi = WiFiManager()
            Logger().log("SUCCESS", "Barcha podsystemalar ishga tushirildi")
            self._initialized = True

    def manage_transport(self):
        print("\nTRANSPORT TIZIMI")
        self.transport.display_status()

    def manage_lighting(self):
        print("\nYORITISH TIZIMI")
        self.lighting.display_lights()

    def access_security_camera(self, password: str):
        print("\nXAVFSIZLIK TIZIMI")
        self.security.proxy.access_cameras(password)

    def monitor_energy(self):
        print("\nENERGIYA TIZIMI")
        self.energy.display_usage()

    def get_weather(self):
        print("\nOB-HAVO")
        self.weather.display_current()

    def manage_waste(self):
        print("\nCHIQINDI TIZIMI")
        self.waste.check_bins()

    def manage_wifi(self):
        print("\nWI-FI TIZIMI")
        self.wifi.display_status()

    def change_traffic_mode(self, mode: str):
        self.transport.set_traffic_mode(mode)

    def full_report(self):
        print("\n" + "="*60)
        print("        SMARTCITY TO'LIQ HISOBOTI")
        print("="*60)
        self.weather.display_current()
        self.energy.display_usage()
        self.security.get_status()
        self.waste.check_bins(report=True)
        self.wifi.display_status()
        self.transport.display_status(report=True)
        print("="*60)