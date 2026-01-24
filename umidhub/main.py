"""
SmartCity System - Main Entry Point
Demonstrates usage of 5 design patterns:
1. Singleton - SmartCityController
2. Factory Method - Vehicle and Light factories
3. Builder - CityConfigBuilder
4. Adapter - SensorAdapter
5. Facade - SmartCityController
"""

from core.controller import SmartCityController
from core.builders.city_config_builder import CityConfigBuilder
from core.factories.transport_factory import BusFactory, TramFactory
from core.factories.lighting_factory import StreetLightFactory, TrafficLightFactory

def main():
    print("╔════════════════════════════════════════╗")
    print("║   SMART CITY MANAGEMENT SYSTEM v1.0    ║")
    print("╚════════════════════════════════════════╝\n")
    
    # Pattern 1 & 5: Singleton + Facade - Get controller instance
    controller = SmartCityController()
    
    # Pattern 3: Builder - Build city configuration
    print("📝 Building city configuration...")
    config = (CityConfigBuilder()
              .set_city_name("Tashkent Smart City")
              .enable_transport()
              .enable_lighting()
              .enable_security()
              .enable_energy_monitoring()
              .enable_sensors()
              .build())
    
    controller.set_configuration(config)
    
    # Pattern 2: Factory Method - Create vehicles
    print("\n🚦 Initializing transport system...")
    bus_factory = BusFactory()
    tram_factory = TramFactory()
    
    bus1 = bus_factory.create_vehicle("12")
    bus2 = bus_factory.create_vehicle("45")
    tram1 = tram_factory.create_vehicle("A")
    
    controller.transport.add_vehicle(bus1)
    controller.transport.add_vehicle(bus2)
    controller.transport.add_vehicle(tram1)
    print("   ✅ 2 buses and 1 tram registered")
    
    # Pattern 2: Factory Method - Create lights
    print("\n💡 Installing lighting system...")
    street_factory = StreetLightFactory()
    traffic_factory = TrafficLightFactory()
    
    light1 = street_factory.create_light("Amir Temur Square")
    light2 = street_factory.create_light("Chorsu Bazaar")
    traffic1 = traffic_factory.create_light("Mustaqillik Ave & Navoi St")
    
    controller.lighting.add_light(light1)
    controller.lighting.add_light(light2)
    controller.lighting.add_light(traffic1)
    print("   ✅ 2 street lights and 1 traffic light installed")
    
    # Setup security
    print("\n🔒 Setting up security system...")
    controller.security.add_camera("City Center")
    controller.security.add_camera("Train Station")
    print("   ✅ 2 cameras installed")
    
    # Setup energy monitoring
    print("\n⚡ Registering energy consumers...")
    controller.energy.register_device("Street Lights", 50)
    controller.energy.register_device("Traffic Lights", 20)
    controller.energy.register_device("Transport System", 100)
    print("   ✅ Energy monitoring active")
    
    # Pattern 5: Facade - Start all systems with single command
    controller.start_city_operations()
    
    # Pattern 4: Adapter - Get sensor data and display status
    controller.get_system_status()
    
    # Energy optimization
    print("\n" + controller.energy.optimize_energy())
    
    # Interactive menu
    print("\n" + "="*50)
    while True:
        print("\n🎛️  CONTROL PANEL")
        print("1. View system status")
        print("2. Check sensor data")
        print("3. Toggle security alarm")
        print("4. Shutdown system")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            controller.get_system_status()
        elif choice == "2":
            # Pattern 4: Adapter in action
            sensor_data = controller.sensors.get_all_sensor_data()
            print("\n📡 Real-time Sensor Data:")
            print(f"   🌤️  Weather: {sensor_data['weather']}")
            print(f"   🚗 Traffic: {sensor_data['traffic']}")
        elif choice == "3":
            if controller.security.alarm_active:
                print(controller.security.deactivate_alarm())
            else:
                print(controller.security.activate_alarm())
        elif choice == "4":
            controller.shutdown()
        elif choice == "5":
            print("\n👋 Exiting Smart City System...")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()