from abc import ABC, abstractmethod


class Light(ABC):
    """Abstract light component"""
    
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def get_brightness(self) -> int:
        pass


class StreetLight(Light):
    """Basic street light"""
    
    def __init__(self, location: str):
        self.location = location
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        print(f"💡 Street light at {self.location} turned ON")
    
    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        print(f"💡 Street light at {self.location} turned OFF")
    
    def get_description(self) -> str:
        return f"Street Light ({self.location})"
    
    def get_brightness(self) -> int:
        return self.brightness


class ParkLight(Light):
    """Park light"""
    
    def __init__(self, location: str):
        self.location = location
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        print(f"💡 Park light at {self.location} turned ON")
    
    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        print(f"💡 Park light at {self.location} turned OFF")
    
    def get_description(self) -> str:
        return f"Park Light ({self.location})"
    
    def get_brightness(self) -> int:
        return self.brightness


class LightDecorator(Light):
    """
    Decorator Pattern Base Class
    Wraps Light objects to add features
    """
    
    def __init__(self, light: Light):
        self._light = light
    
    def turn_on(self):
        self._light.turn_on()
    
    def turn_off(self):
        self._light.turn_off()
    
    def get_description(self) -> str:
        return self._light.get_description()
    
    def get_brightness(self) -> int:
        return self._light.get_brightness()


class DimmableLight(LightDecorator):
    """Decorator: Adds dimming capability"""
    
    def __init__(self, light: Light):
        super().__init__(light)
        self._custom_brightness = 100
    
    def set_brightness(self, level: int):
        """Set brightness level (0-100)"""
        if 0 <= level <= 100:
            self._custom_brightness = level
            if hasattr(self._light, 'brightness'):
                self._light.brightness = level
            print(f"  🔆 Brightness set to {level}%")
        else:
            print(f"  ❌ Invalid brightness level: {level}")
    
    def get_brightness(self) -> int:
        return self._custom_brightness
    
    def get_description(self) -> str:
        return f"{self._light.get_description()} + Dimmable"


class MotionSensorLight(LightDecorator):
    """Decorator: Adds motion detection"""
    
    def __init__(self, light: Light):
        super().__init__(light)
        self.motion_detected = False
    
    def detect_motion(self):
        """Simulate motion detection"""
        self.motion_detected = True
        print(f"  👤 Motion detected - Auto turning on")
        self.turn_on()
    
    def get_description(self) -> str:
        return f"{self._light.get_description()} + Motion Sensor"


class ColorChangingLight(LightDecorator):
    """Decorator: Adds color changing capability"""
    
    def __init__(self, light: Light):
        super().__init__(light)
        self.color = "white"
    
    def set_color(self, color: str):
        """Set light color"""
        self.color = color
        print(f"  🎨 Color changed to {color}")
    
    def get_description(self) -> str:
        return f"{self._light.get_description()} + Color ({self.color})"