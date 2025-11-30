# FIO/main.py

import sys
import os

# Add the FIO directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.controller import SmartCityController
from core.builders.infrastructure_builder import SmartCityBuilder, InfrastructureDirector

def run_system_demonstration():
    """
    Demonstrates the SmartCity System, showcasing the implemented design patterns.
    """
    print("==================================================")
    print("          SMART CITY SYSTEM DEMONSTRATION         ")
    print("==================================================")

    # --- 1. Singleton and Facade Demonstration ---
    # The controller is accessed via the Facade interface, and only one instance exists (Singleton).
    print("\n[1. Singleton and Facade Demonstration]")
    controller1 = SmartCityController()
    controller2 = SmartCityController()
    print(f"Controller 1 ID: {id(controller1)}")
    print(f"Controller 2 ID: {id(controller2)}")
    print(f"Are controllers the same instance? {controller1 is controller2} (Singleton check)")

    controller1.start_city_operations()
    controller1.get_city_status()

    # --- 2. Factory Method Demonstration (Transport Module) ---
    print("\n[2. Factory Method Demonstration (Transport Module)]")
    controller1.manage_transport("bus")
    controller1.manage_transport("tram")
    controller1.manage_transport("taxi")
    controller1.get_city_status()

    # --- 3. Adapter and Decorator Demonstration (Security Module) ---
    print("\n[3. Adapter and Decorator Demonstration (Security Module)]")
    controller1.check_security_feed()

    # --- 4. Proxy Demonstration (Energy Module) ---
    print("\n[4. Proxy Demonstration (Energy Module)]")
    # Access granted
    controller1.request_sensitive_energy_data("Admin")
    # Access denied
    controller1.request_sensitive_energy_data("Citizen")
    controller1.optimize_energy_usage()

    # --- 5. Abstract Factory Demonstration (Lighting Module) ---
    # The Lighting Module is initialized with Basic devices by default.
    # To demonstrate the Abstract Factory, we would need to re-initialize the controller
    # or the module itself, but for simplicity, we rely on the initial setup.
    # The output of start_city_operations already showed the device type.
    print("\n[5. Abstract Factory Demonstration (Lighting Module)]")
    print("The lighting module is currently using Basic devices (see start_city_operations output).")
    print("The Abstract Factory pattern allows easy switching between device families.")

    # --- 6. Builder Demonstration ---
    print("\n[6. Builder Demonstration (Infrastructure Construction)]")
    builder = SmartCityBuilder()
    director = InfrastructureDirector(builder)

    print("Building Full Infrastructure:")
    director.build_full_infrastructure()
    full_infra = builder.get_result()
    full_infra.show_configuration()

    print("Building Minimal Infrastructure:")
    # director.build_minimal_minimal_infrastructure() # Note: This method is not defined in the director, I will use build_minimal_infrastructure
    director.build_minimal_infrastructure()
    minimal_infra = builder.get_result()
    minimal_infra.show_configuration()


if __name__ == "__main__":
    run_system_demonstration()
