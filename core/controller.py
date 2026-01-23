"""
Facade Pattern + Singleton - Simplified interface to complex subsystems
Used for: Central controller that manages all city systems
"""

from core.singleton.singleton_meta import SingletonMeta
from modules.transport.transport_system import TransportSystem
from modules.lighting.lighting_system import LightingSystem
from modules.security.security_system import SecuritySystem
from modules.energy.energy_system import EnergySystem
from core.adapters.sensor_adapter import SensorAdapter

class SmartCityController(metaclass=SingletonMeta):
    """
    Facade Pattern: Provides simplified interface to all subsystems
    Singleton Pattern: Ensures only one controller exists
    """
    
    def __init__(self):
        # Initialize subsystems
        self.transport = TransportSystem()
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.energy = EnergySystem()
        self.sensors = SensorAdapter()
        self.config = None
    
    def set_configuration(self, config):
        self.config = config
        print("✅ Configuration applied!")
        print(config)
    
    def start_city_operations(self):
        """Facade method - starts all enabled systems"""
        print("\n" + "="*50)
        print("🏙️  SMART CITY SYSTEM STARTING...")
        print("="*50 + "\n")
        
        if self.config and self.config.transport_enabled:
            print("🚦 Starting transport system...")
            operations = self.transport.operate_all()
            for op in operations:
                print(f"   {op}")
        
        if self.config and self.config.lighting_enabled:
            print("\n💡 Activating lighting system...")
            lights = self.lighting.turn_all_on()
            for light in lights:
                print(f"   {light}")
        
        if self.config and self.config.security_enabled:
            print("\n" + self.security.activate_alarm())
        
        print("\n✅ All systems operational!")
    
    def get_system_status(self):
        """Facade method - gets status from all systems"""
        print("\n" + "="*50)
        print("📊 SYSTEM STATUS REPORT")
        print("="*50)
        print(self.transport.get_status())
        print(self.lighting.get_status())
        print(self.security.get_status())
        print(self.energy.get_status())
        
        if self.config and self.config.sensor_integration:
            sensor_data = self.sensors.get_all_sensor_data()
            print(f"\n📡 Sensor Data:")
            print(f"   Weather: {sensor_data['weather']['condition']}, "
                  f"{sensor_data['weather']['temperature']}°C")
            print(f"   Traffic: {sensor_data['traffic']['vehicle_count']} vehicles/hour, "
                  f"Congestion: {sensor_data['traffic']['congestion']}")
    
    def shutdown(self):
        """Facade method - safely shuts down all systems"""
        print("\n🔴 Shutting down Smart City System...")
        self.lighting.turn_all_off()
        self.security.deactivate_alarm()
        print("✅ System shutdown complete")