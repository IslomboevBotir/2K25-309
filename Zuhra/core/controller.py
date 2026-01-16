"""
City Controller - Central Management System

Design Patterns Used:
1. SINGLETON: Ensures only one controller instance exists
2. FACADE: Provides unified interface to all subsystems
"""

from modules.transport.transport_manager import TransportManager
from modules.lighting.lighting_manager import LightingManager
from modules.security.security_manager import SecurityManager
from modules.energy.energy_manager import EnergyManager


class CityController:
    """
    Singleton + Facade Pattern
    
    Singleton: Only one controller manages the entire city
    Facade: Simplifies interaction with multiple subsystems
    """
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """Singleton: Ensure only one instance exists"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize subsystems only once"""
        if not CityController._initialized:
            self._city_name = "SmartCity"
            self._status = "Active"
            
            # Initialize all subsystems (Facade Pattern)
            self._transport_manager = TransportManager()
            self._lighting_manager = LightingManager()
            self._security_manager = SecurityManager()
            self._energy_manager = EnergyManager()
            
            CityController._initialized = True
    
    @classmethod
    def get_instance(cls):
        """Get singleton instance"""
        if cls._instance is None:
            cls._instance = CityController()
        return cls._instance
    
    def set_city_name(self, name: str):
        """Set city name"""
        self._city_name = name
    
    def get_city_name(self) -> str:
        """Get city name"""
        return self._city_name
    
    def get_status(self) -> str:
        """Get system status"""
        return self._status
    
    # Facade Methods: Simplified interface to subsystems
    
    def manage_traffic(self, location: str, state: str):
        """Manage traffic lights (Facade)"""
        self._transport_manager.control_traffic_light(location, state)
    
    def manage_public_transport(self, route: str, action: str):
        """Manage public transport (Facade)"""
        self._transport_manager.control_public_transport(route, action)
    
    def control_lighting(self, zone: str, action: str, brightness: int = 100):
        """Control city lighting (Facade)"""
        self._lighting_manager.control_lights(zone, action, brightness)
    
    def monitor_security(self, location: str, device_type: str):
        """Activate security monitoring (Facade)"""
        self._security_manager.activate_device(location, device_type)
    
    def manage_energy(self, location: str, source_type: str):
        """Manage energy sources (Facade)"""
        self._energy_manager.activate_source(location, source_type)
    
    def generate_report(self) -> str:
        """Generate comprehensive city report (Facade)"""
        report = f"\n{'='*50}\n"
        report += f"SMART CITY REPORT: {self._city_name}\n"
        report += f"{'='*50}\n\n"
        
        report += "🚦 Transportation Status:\n"
        report += self._transport_manager.get_status() + "\n\n"
        
        report += "💡 Lighting Status:\n"
        report += self._lighting_manager.get_status() + "\n\n"
        
        report += "🔒 Security Status:\n"
        report += self._security_manager.get_status() + "\n\n"
        
        report += "⚡ Energy Status:\n"
        report += self._energy_manager.get_status() + "\n"
        
        report += f"{'='*50}\n"
        return report