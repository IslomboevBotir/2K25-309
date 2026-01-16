"""
Lighting Manager - Uses Decorator Pattern
"""

from modules.lighting.lighting_system import (
    Light, StreetLight, ParkLight, 
    DimmableLight, MotionSensorLight, ColorChangingLight
)


class LightingManager:
    """Manages all lighting devices using decorators"""
    
    def __init__(self):
        self._lights = {}
    
    def control_lights(self, zone: str, action: str, brightness: int = 100):
        """Control lights in a zone"""
        if zone not in self._lights:
            # Create new light with decorators
            if "park" in zone.lower():
                base_light = ParkLight(zone)
            else:
                base_light = StreetLight(zone)
            
            # Add decorators based on zone
            decorated_light = DimmableLight(base_light)
            if "downtown" in zone.lower():
                decorated_light = ColorChangingLight(decorated_light)
            
            self._lights[zone] = decorated_light
            print(f"✓ Installed: {decorated_light.get_description()}")
        
        light = self._lights[zone]
        
        if action == "on":
            light.turn_on()
            if isinstance(light, DimmableLight):
                light.set_brightness(brightness)
        elif action == "off":
            light.turn_off()
        elif action == "dim":
            if isinstance(light, DimmableLight):
                light.set_brightness(brightness)
            else:
                print(f"  ❌ Light is not dimmable")
    
    def get_status(self) -> str:
        """Get status of all lights"""
        if not self._lights:
            return "  No lights installed"
        
        status = ""
        for zone, light in self._lights.items():
            brightness = light.get_brightness()
            state = "ON" if brightness > 0 else "OFF"
            status += f"  - {zone}: {state} ({brightness}%)\n"
            status += f"    Type: {light.get_description()}\n"
        
        return status