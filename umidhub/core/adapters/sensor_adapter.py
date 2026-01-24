"""
Adapter Pattern - allows incompatible interfaces to work together
Used for: Integrating external weather/traffic sensors
"""

class ExternalWeatherSensor:
    """Simulates external API with different interface"""
    def fetch_temperature_data(self):
        return {"temp_celsius": 24, "humidity": 65}
    
    def fetch_weather_condition(self):
        return "Sunny"


class ExternalTrafficSensor:
    """Simulates external traffic monitoring system"""
    def get_traffic_density(self):
        return {"cars_per_hour": 450, "congestion_level": "Medium"}


class SensorAdapter:
    """Adapter that converts external sensor data to our system format"""
    
    def __init__(self):
        self.weather_sensor = ExternalWeatherSensor()
        self.traffic_sensor = ExternalTrafficSensor()
    
    def get_weather_data(self):
        """Unified interface for weather data"""
        temp_data = self.weather_sensor.fetch_temperature_data()
        condition = self.weather_sensor.fetch_weather_condition()
        
        return {
            "temperature": temp_data["temp_celsius"],
            "humidity": temp_data["humidity"],
            "condition": condition
        }
    
    def get_traffic_data(self):
        """Unified interface for traffic data"""
        traffic = self.traffic_sensor.get_traffic_density()
        
        return {
            "vehicle_count": traffic["cars_per_hour"],
            "congestion": traffic["congestion_level"]
        }
    
    def get_all_sensor_data(self):
        return {
            "weather": self.get_weather_data(),
            "traffic": self.get_traffic_data()
        }