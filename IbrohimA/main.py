"""
SmartCity System - Main Application Entry Point

This application demonstrates a comprehensive smart city management system
with multiple design patterns implemented:

1. SINGLETON - SmartCityController (single instance)
2. FACTORY METHOD - Device creation factories
3. ABSTRACT FACTORY - Subsystem device families
4. BUILDER - System configuration building
5. PROXY - Subsystem access control & lazy initialization
6. DECORATOR - Enhanced functionality (monitoring, security, logging)
7. FACADE - Unified interface to all subsystems
"""

from core.controller import SmartCityController
from core.builders.builders import SmartCityBuilder
from modules.lighting.lighting_devices import SmartLight
from modules.security.security_devices import SecurityCamera
from modules.transport.transport_devices import TrafficLight
from modules.energy.energy_devices import EnergyMonitor
import json


def display_welcome():
    """Display welcome message"""
    print("\n" + "="*70)
    print("╔" + "═"*68 + "╗")
    print("║" + " "*15 + "🏙️  SMARTCITY MANAGEMENT SYSTEM 🏙️" + " "*16 + "║")
    print("║" + " "*68 + "║")
    print("║" + "  Advanced urban infrastructure control with Design Patterns" + " "*5 + "║")
    print("╚" + "═"*68 + "╝")
    print("="*70 + "\n")


def display_patterns_info():
    """Display information about implemented patterns"""
    print("\n" + "-"*70)
    print("📋 IMPLEMENTED DESIGN PATTERNS:")
    print("-"*70)
    
    patterns = {
        "1. SINGLETON": "SmartCityController - Ensures single instance for central control",
        "2. FACTORY METHOD": "Individual device factories for each subsystem type",
        "3. ABSTRACT FACTORY": "Family of device factories for creating related objects",
        "4. BUILDER": "SmartCityBuilder - Complex system configuration construction",
        "5. PROXY": "SubsystemProxy - Access control and lazy initialization",
        "6. DECORATOR": "MonitoringDecorator, SecurityDecorator, LoggingDecorator",
        "7. FACADE": "Controller provides unified interface to all subsystems"
    }
    
    for pattern, description in patterns.items():
        print(f"\n  {pattern}")
        print(f"     └─ {description}")
    
    print("\n" + "-"*70 + "\n")


def demo_factory_pattern(controller):
    """Demonstrate Factory Pattern"""
    print("\n" + "="*70)
    print("🏭 DEMONSTRATING FACTORY PATTERN")
    print("="*70)
    
    print("\n[Creating devices using different factories...]")
    
    # Create lighting device
    light = controller.create_device('lighting', 'LIGHT-MAIN-01', 'Main Street')
    controller.add_device_to_subsystem('lighting', 'LIGHT-MAIN-01', light)
    
    # Create security camera
    camera = controller.create_device('security', 'CAM-DOWNTOWN-01', 'Downtown')
    controller.add_device_to_subsystem('security', 'CAM-DOWNTOWN-01', camera)
    
    # Create traffic light
    traffic = controller.create_device('transport', 'TRAFFIC-MAIN-01', 'Main Intersection')
    controller.add_device_to_subsystem('transport', 'TRAFFIC-MAIN-01', traffic)
    
    # Create energy monitor
    energy = controller.create_device('energy', 'ENERGY-ZONE-01', 'Zone A')
    controller.add_device_to_subsystem('energy', 'ENERGY-ZONE-01', energy)
    
    print("\n✓ All devices created successfully using their respective factories\n")


def demo_builder_pattern():
    """Demonstrate Builder Pattern"""
    print("\n" + "="*70)
    print("🔨 DEMONSTRATING BUILDER PATTERN")
    print("="*70)
    
    print("\n[Building SmartCity configuration using method chaining...]")
    
    config = (SmartCityBuilder("MySmartCity")
             .add_lighting_system(5, ["Main St", "Oak Ave", "Park Ln", "River Rd", "Hill St"])
             .add_security_system(3, ["Downtown", "Harbor", "Airport"])
             .add_transport_system(4, ["Main-Oak", "River-Park", "Oak-Hill", "Main-River"])
             .add_energy_system(2, ["Zone A", "Zone B"])
             .set_auto_start(True)
             .enable_logging(True)
             .build())
    
    print(f"\n✓ Configuration built for: {config.city_name}")
    print(f"  - Lighting devices: {config.num_lighting_devices}")
    print(f"  - Security cameras: {config.num_security_cameras}")
    print(f"  - Traffic lights: {config.num_traffic_lights}")
    print(f"  - Energy monitors: {config.num_energy_monitors}")
    print(f"  - Auto-start: {config.auto_start}")
    print(f"  - Logging enabled: {config.log_enabled}\n")


def demo_singleton_pattern():
    """Demonstrate Singleton Pattern"""
    print("\n" + "="*70)
    print("🔐 DEMONSTRATING SINGLETON PATTERN")
    print("="*70)
    
    print("\n[Creating multiple SmartCityController instances...]")
    
    # Create multiple instances
    controller1 = SmartCityController()
    controller2 = SmartCityController()
    controller3 = SmartCityController()
    
    print(f"Controller 1 ID: {id(controller1)}")
    print(f"Controller 2 ID: {id(controller2)}")
    print(f"Controller 3 ID: {id(controller3)}")
    
    if id(controller1) == id(controller2) == id(controller3):
        print("\n✓ All instances are identical - Singleton pattern working!\n")
    else:
        print("\n✗ Instances differ - Singleton failed!\n")


def demo_proxy_and_decorators(controller):
    """Demonstrate Proxy and Decorator Patterns"""
    print("\n" + "="*70)
    print("🛡️  DEMONSTRATING PROXY & DECORATOR PATTERNS")
    print("="*70)
    
    print("\n[Using Proxy for access control and lazy initialization...]")
    print("[Using Decorators to add monitoring, security, and logging...]")
    
    status = controller.get_subsystem_status('security')
    print(f"\nSecurity System Status:")
    print(json.dumps(status, indent=2)[:300] + "...\n")
    
    print("✓ Proxy controls access to subsystems")
    print("✓ Decorators add enhanced functionality\n")


def interactive_menu(controller):
    """Interactive menu for system control"""
    print("\n" + "="*70)
    print("🎮 INTERACTIVE CONTROL PANEL")
    print("="*70)
    
    while True:
        controller.display_menu()
        
        choice = input("\nEnter your choice (0-7): ").strip()
        
        if choice == '0':
            print("\nExiting system...")
            break
        
        elif choice == '1':
            print("\n📊 SYSTEM STATUS:")
            print("-"*70)
            status = controller.get_all_status()
            print(json.dumps(status, indent=2))
        
        elif choice == '2':
            controller.start_all_subsystems()
        
        elif choice == '3':
            controller.stop_all_subsystems()
        
        elif choice == '4':
            print("\n[Create and Add Device]")
            subsystem = input("Subsystem (lighting/security/transport/energy): ").strip()
            device_id = input("Device ID: ").strip()
            location = input("Location: ").strip()
            
            device = controller.create_device(subsystem, device_id, location)
            if device:
                controller.add_device_to_subsystem(subsystem, device_id, device)
        
        elif choice == '5':
            subsystem = input("Subsystem (lighting/security/transport/energy): ").strip()
            controller.start_subsystem(subsystem)
        
        elif choice == '6':
            subsystem = input("Subsystem (lighting/security/transport/energy): ").strip()
            controller.stop_subsystem(subsystem)
        
        elif choice == '7':
            print("\n" + "="*70)
            print("SYSTEM INFORMATION")
            print("="*70)
            print("\n🏙️  SmartCity System v1.0")
            print("Design Patterns: Singleton, Factory, Abstract Factory, Builder")
            print("                 Proxy, Decorator, Facade")
            print("\n📡 Subsystems:")
            print("  - Lighting Management System")
            print("  - Security Surveillance System")
            print("  - Transportation Control System")
            print("  - Energy Monitoring System")
            print("\n✨ Features:")
            print("  - Multi-subsystem integration")
            print("  - Real-time device management")
            print("  - Access control and monitoring")
            print("  - Extensible architecture")
            print("\n" + "="*70 + "\n")
        
        else:
            print("\n❌ Invalid choice. Please try again.")


def main():
    """Main application entry point"""
    display_welcome()
    display_patterns_info()
    
    # Initialize controller (Singleton)
    controller = SmartCityController()
    controller.initialize()
    
    # Demonstrate design patterns
    print("\n" + "█"*70)
    print("DESIGN PATTERNS DEMONSTRATION")
    print("█"*70)
    
    # 1. Singleton Demo
    demo_singleton_pattern()
    
    # 2. Builder Demo
    demo_builder_pattern()
    
    # 3. Factory Demo
    demo_factory_pattern(controller)
    
    # 4. Proxy & Decorator Demo
    demo_proxy_and_decorators(controller)
    
    print("\n" + "█"*70)
    print("INITIALIZATION COMPLETE")
    print("█"*70)
    
    # Interactive menu
    try:
        interactive_menu(controller)
    except KeyboardInterrupt:
        print("\n\nKeyboard interrupt detected...")
    finally:
        controller.shutdown()
        print("\n✓ Application terminated successfully\n")


if __name__ == '__main__':
    main()
