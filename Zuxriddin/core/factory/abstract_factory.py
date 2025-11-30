# core/controller.py

from modules.lighting.manager import LightingManager
from modules.transport.manager import TransportManager


# ... import other managers

class SmartCityController:
    """
    DESIGN PATTERN: SINGLETON
    Ensures only one instance of the controller exists to manage the city.

    DESIGN PATTERN: FACADE
    Provides a simplified, high-level interface (Facade) to the client
    for interacting with the complex subsystems (LightingManager, etc.).
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartCityController, cls).__new__(cls)
            # Initialize subsystems here
            cls._instance.lighting_manager = LightingManager()
            cls._instance.transport_manager = TransportManager()
            print("SmartCity System Initialized.")
        return cls._instance

    # FACADE Methods: Simplify complex operations
    def optimize_city_systems(self):
        """A single call to optimize energy and traffic."""
        print("\n--- Running City Optimization ---")
        self.lighting_manager.optimize_lighting_for_weather()
        self.transport_manager.adjust_traffic_flow()
        print("Optimization Complete.")

    def get_system_status(self):
        """Facade method to get a summarized status."""
        l_status = self.lighting_manager.get_status()
        t_status = self.transport_manager.get_status()
        return f"Lighting: {l_status} | Transport: {t_status}"


# Example of a simplified Singleton access
SmartCitySystem = SmartCityController