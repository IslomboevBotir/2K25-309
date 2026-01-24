"""
Factory Method Pattern - for creating different types of lights
Used for: Street lights, traffic lights, decorative lights
"""

from abc import ABC, abstractmethod

class Light(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_brightness(self):
        pass


class StreetLight(Light):
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.brightness = 0
    
    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        return f"💡 Street light at {self.location} turned ON (100%)"
    
    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        return f"💡 Street light at {self.location} turned OFF"
    
    def get_brightness(self):
        return self.brightness


class TrafficLight(Light):
    def __init__(self, intersection):
        self.intersection = intersection
        self.current_signal = "RED"
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        return f"🚦 Traffic light at {self.intersection} activated - Signal: {self.current_signal}"
    
    def turn_off(self):
        self.is_on = False
        return f"🚦 Traffic light at {self.intersection} deactivated"
    
    def get_brightness(self):
        return 100 if self.is_on else 0


class LightFactory(ABC):
    @abstractmethod
    def create_light(self, identifier):
        pass


class StreetLightFactory(LightFactory):
    def create_light(self, location):
        return StreetLight(location)


class TrafficLightFactory(LightFactory):
    def create_light(self, intersection):
        return TrafficLight(intersection)