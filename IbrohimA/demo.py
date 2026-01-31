#!/usr/bin/env python3
"""
Demo Script - Automated SmartCity System Demonstration
Shows all patterns in action without interactive input
"""

from core.controller import SmartCityController
from core.builders.builders import SmartCityBuilder
from modules.lighting.lighting_devices import SmartLight
import time
import json


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def demo_full_system():
    """Run full automated demonstration"""
    
    print_section("🏙️  SMARTCITY SYSTEM - FULL DEMONSTRATION")
    
    # ==================== BUILDER PATTERN ====================
    print_section("1️⃣  BUILDER PATTERN - System Configuration")
    print("\nBuilding SmartCity configuration using fluent interface...")
    
    config = (SmartCityBuilder("San Francisco Smart City")
        .add_lighting_system(8, [
            "Market Street", "Mission Street", "Valencia Street",
            "Haight Street", "Fillmore Street", "Castro Street",
            "Oak Street", "Fell Street"
        ])
        .add_security_system(5, [
            "Downtown", "Waterfront", "Financial District", 
            "North Beach", "SoMa"
        ])
        .add_transport_system(12, [
            "Market-Mission", "Mission-Valencia", "Valencia-Haight",
            "Haight-Fillmore", "Fillmore-Castro", "Castro-Oak",
            "Oak-Fell", "Fell-Van Ness", "Van Ness-Market",
            "Market-Grant", "Grant-Kearny", "Kearny-Montgomery"
        ])
        .add_energy_system(6, [
            "Downtown Zone", "Waterfront Zone", "Financial District Zone",
            "Residential Zone A", "Residential Zone B", "Residential Zone C"
        ])
        .set_auto_start(True)
        .enable_logging(True)
        .build())
    
    print(f"\n✅ Configuration Built Successfully!")
    print(f"   City: {config.city_name}")
    print(f"   Lighting systems: {config.num_lighting_devices}")
    print(f"   Security cameras: {config.num_security_cameras}")
    print(f"   Traffic lights: {config.num_traffic_lights}")
    print(f"   Energy monitors: {config.num_energy_monitors}")
    print(f"   Auto-start: {config.auto_start}")
    print(f"   Logging: {config.log_enabled}")
    
    # ==================== SINGLETON PATTERN ====================
    print_section("2️⃣  SINGLETON PATTERN - Unique Controller Instance")
    print("\nCreating multiple controller instances...")
    
    controller1 = SmartCityController()
    controller2 = SmartCityController()
    controller3 = SmartCityController()
    
    print(f"Controller 1 ID: {id(controller1)}")
    print(f"Controller 2 ID: {id(controller2)}")
    print(f"Controller 3 ID: {id(controller3)}")
    
    if id(controller1) == id(controller2) == id(controller3):
        print(f"\n✅ Singleton Pattern Verified!")
        print(f"   All controllers point to same instance")
    
    # ==================== SYSTEM INITIALIZATION ====================
    print_section("3️⃣  SYSTEM INITIALIZATION")
    print("\nInitializing SmartCity Controller and all subsystems...")
    
    controller = controller1  # Use the singleton instance
    controller._initialized = False  # Reset for demo
    controller._is_running = False
    controller.initialize()
    
    # ==================== FACTORY PATTERN ====================
    print_section("4️⃣  FACTORY PATTERN - Device Creation")
    print("\nCreating devices using specialized factories...")
    
    devices = []
    
    # Create lighting devices
    print("\n[Lighting Factory]")
    for i, location in enumerate(config.device_configs['lighting']['locations'][:3], 1):
        light = controller.create_device('lighting', f'LIGHT-{i:03d}', location)
        devices.append(('lighting', f'LIGHT-{i:03d}', light))
        controller.add_device_to_subsystem('lighting', f'LIGHT-{i:03d}', light)
    
    # Create security devices
    print("\n[Security Factory]")
    for i, location in enumerate(config.device_configs['security']['locations'][:2], 1):
        camera = controller.create_device('security', f'CAM-{i:03d}', location)
        devices.append(('security', f'CAM-{i:03d}', camera))
        controller.add_device_to_subsystem('security', f'CAM-{i:03d}', camera)
    
    # Create transport devices
    print("\n[Transport Factory]")
    for i, intersection in enumerate(config.device_configs['transport']['intersections'][:3], 1):
        traffic = controller.create_device('transport', f'TRAFFIC-{i:03d}', intersection)
        devices.append(('transport', f'TRAFFIC-{i:03d}', traffic))
        controller.add_device_to_subsystem('transport', f'TRAFFIC-{i:03d}', traffic)
    
    # Create energy devices
    print("\n[Energy Factory]")
    for i, zone in enumerate(config.device_configs['energy']['zones'][:2], 1):
        monitor = controller.create_device('energy', f'ENERGY-{i:03d}', zone)
        devices.append(('energy', f'ENERGY-{i:03d}', monitor))
        controller.add_device_to_subsystem('energy', f'ENERGY-{i:03d}', monitor)
    
    print(f"\n✅ Total devices created: {len(devices)}")
    
    # ==================== PROXY & DECORATOR PATTERNS ====================
    print_section("5️⃣  PROXY & DECORATOR PATTERNS - Access Control & Monitoring")
    print("\nProxy provides lazy initialization and access control...")
    print("Decorators add monitoring, security, and logging capabilities...")
    
    print("\n[Accessing Subsystems through Proxy]")
    for subsystem in ['lighting', 'security', 'transport', 'energy']:
        status = controller.get_subsystem_status(subsystem)
        print(f"\n  {status['system_name']}")
        print(f"    - Running: {status.get('is_running', 'N/A')}")
        print(f"    - Devices: {status.get('device_count', 'N/A')}")
    
    # ==================== DEVICE OPERATIONS ====================
    print_section("6️⃣  OPERATING DEVICES")
    print("\nStarting all subsystems and devices...")
    
    controller.start_all_subsystems()
    time.sleep(1)
    
    print("\n[Subsystem Operations]")
    
    # Get lighting status
    lighting_status = controller.get_subsystem_status('lighting')
    if lighting_status.get('devices'):
        print(f"\n  Lighting: {len(lighting_status['devices'])} devices online")
        for device_id, info in list(lighting_status['devices'].items())[:2]:
            print(f"    - {device_id}: Brightness {info['brightness']}%")
    
    # Get security status
    security_status = controller.get_subsystem_status('security')
    if security_status.get('devices'):
        print(f"\n  Security: {len(security_status['devices'])} cameras online")
        for device_id, info in list(security_status['devices'].items())[:2]:
            recording = "🔴 RECORDING" if info['is_recording'] else "⚪ OFF"
            print(f"    - {device_id}: {recording}")
    
    # Get transport status
    transport_status = controller.get_subsystem_status('transport')
    if transport_status.get('devices'):
        print(f"\n  Transport: {len(transport_status['devices'])} traffic lights online")
        for device_id, info in list(transport_status['devices'].items())[:2]:
            print(f"    - {device_id}: Signal = {info['current_signal'].upper()}")
    
    # Get energy status
    energy_status = controller.get_subsystem_status('energy')
    if energy_status.get('devices'):
        print(f"\n  Energy: {len(energy_status['devices'])} monitors online")
    
    # ==================== FACADE PATTERN ====================
    print_section("7️⃣  FACADE PATTERN - Unified System Interface")
    print("\nController provides unified interface for all operations...")
    
    print("\n[System-wide Status Report]")
    all_status = controller.get_all_status()
    print(f"  Controller Running: {all_status['controller_running']}")
    print(f"  Active Subsystems: {len(all_status['subsystems'])}")
    for subsys_name in all_status['subsystems']:
        print(f"    ✓ {subsys_name.capitalize()} System")
    
    # ==================== ADVANCED OPERATIONS ====================
    print_section("8️⃣  ADVANCED OPERATIONS")
    
    print("\nDemonstrating selective subsystem control...")
    print("\n[Stopping Lighting Subsystem Only]")
    controller.stop_subsystem('lighting')
    
    print("\n[Stopping Security Subsystem Only]")
    controller.stop_subsystem('security')
    
    time.sleep(0.5)
    
    print("\n[Restarting All Subsystems]")
    controller.start_all_subsystems()
    
    # ==================== FINAL STATUS ====================
    print_section("9️⃣  FINAL SYSTEM STATUS")
    
    final_status = controller.get_all_status()
    print(json.dumps(final_status, indent=2)[:500] + "\n  ...")
    
    # ==================== SHUTDOWN ====================
    print_section("🔟 SYSTEM SHUTDOWN")
    print("\nGracefully shutting down all subsystems...")
    
    controller.stop_all_subsystems()
    controller.shutdown()
    
    # ==================== SUMMARY ====================
    print_section("✅ DEMONSTRATION COMPLETE")
    
    print("""
🎉 SmartCity System Successfully Demonstrated!

📊 Patterns Showcased:
  1. ✓ SINGLETON - Single controller instance
  2. ✓ FACTORY METHOD - Individual device factories
  3. ✓ ABSTRACT FACTORY - Family of factories
  4. ✓ BUILDER - Configuration building
  5. ✓ PROXY - Access control & lazy initialization
  6. ✓ DECORATOR - Monitoring, security, logging
  7. ✓ FACADE - Unified system interface

🏆 System Features:
  ✓ Multi-subsystem integration
  ✓ Device management
  ✓ Real-time monitoring
  ✓ Extensible architecture
  ✓ Access control
  ✓ Comprehensive logging

👨‍💻 Ready for production-grade smart city operations!
    """)


if __name__ == '__main__':
    try:
        demo_full_system()
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
