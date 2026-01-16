"""
Security Manager - Uses Proxy Pattern
"""

from modules.security.security_system import (
    Camera, AlarmSystem, SecurityDeviceProxy
)


class SecurityManager:
    """Manages all security devices through proxies"""
    
    def __init__(self):
        self._devices = {}
        self._default_access = "admin"  # Default to admin for demo
    
    def activate_device(self, location: str, device_type: str):
        """Activate security device at location"""
        if location not in self._devices:
            # Create real device
            if device_type == "camera":
                real_device = Camera(location)
            elif device_type == "alarm":
                real_device = AlarmSystem(location)
            else:
                print(f"❌ Unknown device type: {device_type}")
                return
            
            # Wrap in proxy for access control
            proxy = SecurityDeviceProxy(real_device, self._default_access)
            self._devices[location] = proxy
            print(f"✓ Installed {device_type} at {location}")
        
        # Activate through proxy (checks access)
        self._devices[location].activate()
        self._devices[location].monitor()
    
    def monitor_location(self, location: str):
        """Monitor a specific location"""
        if location in self._devices:
            self._devices[location].monitor()
        else:
            print(f"❌ No security device at {location}")
    
    def get_status(self) -> str:
        """Get status of all security devices"""
        if not self._devices:
            return "  No security devices installed"
        
        status = ""
        for location, proxy in self._devices.items():
            status += f"  - {proxy.get_status()}\n"
        
        return status