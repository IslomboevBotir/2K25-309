from core.event_manager import EventManager
from modules.lighting.lighting_factory import LightingSystemFactory
from modules.transport.transport_factory import TransportSystemFactory
from modules.security.cameras import SecurityCameraSystem
from modules.energy.meters import EnergyMeterSystem

class SmartCityController:
    """Facade pattern: Provides a simplified interface to the entire SmartCity system."""
    _instance = None

    def __new__(cls):
        """Singleton pattern: Ensures only one controller instance exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.event_manager = EventManager()
            cls._instance._initialize_subsystems()
        return cls._instance

    def _initialize_subsystems(self):
        self.lighting = LightingSystemFactory.create_system()
        self.transport = TransportSystemFactory.create_system()
        self.security = SecurityCameraSystem()
        self.energy = EnergyMeterSystem()

    def start_city(self):
        print("🚀 SmartCity System Activated!")
        self.lighting.turn_on()
        self.transport.start_service()
        self.security.activate()
        self.energy.start_monitoring()

    def simulate_event(self, event_type):
        print(f"\n🔔 Simulating event: {event_type}")
        self.event_manager.notify(event_type)

    def stop_city(self):
        print("\n🛑 SmartCity System Shutting Down...")
        self.lighting.turn_off()
        self.transport.stop_service()
        self.security.deactivate()
        self.energy.stop_monitoring()