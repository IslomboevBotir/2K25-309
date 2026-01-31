"""
Lighting subsystem module
Smart lighting device implementation
"""


class SmartLight:
    """Smart light device for streetlights"""
    
    def __init__(self, device_id: str, location: str):
        self.device_id = device_id
        self.location = location
        self.is_on = False
        self.brightness = 0  # 0-100%
    
    def start(self):
        """Turn on the light"""
        self.is_on = True
        self.brightness = 100
        print(f"[LIGHT] {self.device_id} at {self.location}: ON (Brightness: 100%)")
    
    def stop(self):
        """Turn off the light"""
        self.is_on = False
        self.brightness = 0
        print(f"[LIGHT] {self.device_id} at {self.location}: OFF")
    
    def status(self) -> dict:
        """Get light status"""
        return {
            'device_id': self.device_id,
            'location': self.location,
            'is_on': self.is_on,
            'brightness': self.brightness
        }
    
    def set_brightness(self, level: int):
        """Set brightness level (0-100)"""
        self.brightness = max(0, min(100, level))
        print(f"[LIGHT] {self.device_id}: Brightness set to {self.brightness}%")
