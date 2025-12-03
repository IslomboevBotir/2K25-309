from modules.lighting.lighting_module import LightingModule
from modules.transport.transport_module import TransportModule
from modules.security.security_module import SecurityModule
from modules.energy.energy_module import EnergyModule
from core.adapter.weather_adapter import WeatherAdapter, WeatherProvider
from core.builder.traffic_builder import TrafficBuilder

class Controller:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Important: Avoid reinitialization of subsystems if instance already created
        if hasattr(self, "_initialized") and self._initialized:
            return

        # Initialize subsystems once
        self.lighting = LightingModule()
        self.transport = TransportModule()
        self.security = SecurityModule()
        self.energy = EnergyModule()

        # Adapter & Builder
        self.weather_adapter = WeatherAdapter(WeatherProvider())
        self.traffic_builder = TrafficBuilder()

        self._initialized = True
        self._initialization = True


    # Facade methods
    def system_status(self):
        print("\n--- 🏙 SMART CITY SYSTEM STATUS ---")
        self.lighting.status()
        self.transport.status()
        self.security.status()
        self.energy.status()
        print("--------------------------------\n")

    def start_traffic_system(self):
        self.transport.start()

    def toggle_city_lights(self, state: bool):
        if state:
            self.lighting.root_group.turn_on()
        else:
            self.lighting.root_group.turn_off()

    def detect_threat(self, threat: str):
        self.security.trigger_alarm(threat)

    def monitor_energy(self):
        self.energy.monitor()

    def simulate_weather(self):
        data = self.weather_adapter.get_weather()
        print(f"🌦 Weather: {data.condition}, Temperature: {data.temperature}°C")
