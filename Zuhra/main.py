"""
SmartCity System - Main Entry Point
Demonstrates all design patterns in action
"""

from core.controller import CityController
from modules.transport.transport_system import TrafficLight, PublicTransport
from modules.lighting.lighting_system import StreetLight, ParkLight
from modules.security.security_system import Camera, AlarmSystem
from modules.energy.energy_system import SolarPanel, WindTurbine


def main():
    """Main application demonstrating SmartCity System"""
    
    print("=" * 60)
    print("🏙️  SMART CITY MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Get singleton instance of city controller (Singleton Pattern)
    controller = CityController.get_instance()
    controller.set_city_name("TechnoCity")
    
    print(f"\n✓ Initialized: {controller.get_city_name()}")
    print(f"✓ System Status: {controller.get_status()}\n")
    
    # Demonstrate subsystem operations
    print("=" * 60)
    print("📊 SUBSYSTEM DEMONSTRATIONS")
    print("=" * 60)
    
    # 1. Transportation System
    print("\n🚦 TRANSPORTATION SYSTEM")
    print("-" * 40)
    controller.manage_traffic("Main St & 1st Ave", "green")
    controller.manage_traffic("Park Rd & 2nd St", "red")
    controller.manage_public_transport("Bus Route 42", "start")
    
    # 2. Lighting System
    print("\n💡 LIGHTING SYSTEM")
    print("-" * 40)
    controller.control_lighting("Downtown Area", "on", 100)
    controller.control_lighting("Park Zone", "dim", 30)
    
    # 3. Security System
    print("\n🔒 SECURITY SYSTEM")
    print("-" * 40)
    controller.monitor_security("City Hall", "camera")
    controller.monitor_security("Bank District", "alarm")
    
    # 4. Energy Management
    print("\n⚡ ENERGY MANAGEMENT")
    print("-" * 40)
    controller.manage_energy("Solar Farm A", "solar")
    controller.manage_energy("Wind Farm B", "wind")
    
    # Get system report
    print("\n" + "=" * 60)
    print("📈 SYSTEM REPORT")
    print("=" * 60)
    report = controller.generate_report()
    print(report)
    
    # Interactive menu
    print("\n" + "=" * 60)
    print("🎮 INTERACTIVE MODE")
    print("=" * 60)
    
    while True:
        print("\nAvailable Commands:")
        print("  1. Check system status")
        print("  2. Control traffic light")
        print("  3. Control street lighting")
        print("  4. Activate security")
        print("  5. Monitor energy")
        print("  6. Generate full report")
        print("  0. Exit")
        
        choice = input("\nEnter command number: ").strip()
        
        if choice == "0":
            print("\n👋 Shutting down SmartCity System...")
            break
        elif choice == "1":
            print(f"\n✓ Status: {controller.get_status()}")
        elif choice == "2":
            location = input("  Enter intersection: ")
            state = input("  Enter state (green/yellow/red): ")
            controller.manage_traffic(location, state)
        elif choice == "3":
            zone = input("  Enter zone: ")
            action = input("  Enter action (on/off/dim): ")
            if action == "dim":
                brightness = int(input("  Enter brightness (0-100): "))
            else:
                brightness = 100 if action == "on" else 0
            controller.control_lighting(zone, action, brightness)
        elif choice == "4":
            location = input("  Enter location: ")
            device_type = input("  Enter type (camera/alarm): ")
            controller.monitor_security(location, device_type)
        elif choice == "5":
            location = input("  Enter location: ")
            source_type = input("  Enter type (solar/wind): ")
            controller.manage_energy(location, source_type)
        elif choice == "6":
            print("\n" + controller.generate_report())
        else:
            print("❌ Invalid command")
    
    print("✓ System shutdown complete")
    print("=" * 60)


if __name__ == "__main__":
    main()