"""
Lighting Management Subsystem
"""

class LightingSystem:
    def __init__(self):
        self.lights = []
    
    def add_light(self, light):
        self.lights.append(light)
    
    def turn_all_on(self):
        results = []
        for light in self.lights:
            results.append(light.turn_on())
        return results
    
    def turn_all_off(self):
        results = []
        for light in self.lights:
            results.append(light.turn_off())
        return results
    
    def get_status(self):
        if not self.lights:
            return "💡 Lighting System: No lights installed"
        
        status = "💡 Lighting System Status:\n"
        for light in self.lights:
            brightness = light.get_brightness()
            status += f"   - Brightness: {brightness}%\n"
        return status