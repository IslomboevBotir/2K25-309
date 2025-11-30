# FIO/core/controller.py

from FIO.core.singleton.singleton import Singleton
from FIO.modules.transport.transport_module import TransportModule
from FIO.modules.lighting.lighting_module import LightingModule
from FIO.modules.security.security_module import SecurityModule
from FIO.modules.energy.energy_module import EnergyModule

class SmartCityController(metaclass=Singleton):
    """
    Design Pattern: Singleton (Creational)
    Purpose: Ensures that only one instance of the central controller exists.
    
    Design Pattern: Facade (Structural)
    Purpose: Provides a simplified, unified interface to a set of interfaces in the subsystems.
             Clients interact with the controller instead of the complex subsystem logic.
    """
    def __init__(self):
        print("SmartCityController initialized (Singleton instance created).")
        self._transport_module = TransportModule()
        self._lighting_module = LightingModule()
        self._security_module = SecurityModule()
        self._energy_module = EnergyModule()

    # --- Facade Methods ---

    def start_city_operations(self):
        """Starts all core city operations."""
        print("\n--- Starting Smart City Operations ---")
        self._transport_module.start_traffic_control()
        self._lighting_module.activate_smart_lighting()
        self._security_module.deploy_security_system()
        self._energy_module.start_monitoring()
        print("--- All core operations are active. ---")

    def optimize_energy_usage(self):
        """Optimizes energy usage across the city."""
        print("\n--- Optimizing Energy Usage ---")
        self._lighting_module.adjust_brightness_for_saving()
        self._energy_module.report_usage()
        print("--- Optimization complete. ---")

    def get_city_status(self):
        """Retrieves the current status of all major subsystems."""
        print("\n--- Smart City Status Report ---")
        self._transport_module.get_status()
        self._lighting_module.get_status()
        self._security_module.get_status()
        self._energy_module.get_status()
        print("--- End of Status Report ---")

    def manage_transport(self, vehicle_type):
        """Manages transport operations using the Factory Method."""
        print(f"\n--- Managing Transport: Creating a {vehicle_type} ---")
        self._transport_module.create_vehicle(vehicle_type)

    def check_security_feed(self):
        """Checks the security feed, demonstrating the Adapter pattern."""
        print("\n--- Checking Security Feed ---")
        self._security_module.check_feed()

    def request_sensitive_energy_data(self, user_role):
        """Requests sensitive energy data, demonstrating the Proxy pattern."""
        print(f"\n--- Requesting Sensitive Energy Data as {user_role} ---")
        self._energy_module.get_sensitive_data(user_role)

    # Add more facade methods as needed to expose subsystem functionality
