import random

class ExternalWeatherService:
    def get_current(self):
        choices = ['sunny', 'cloudy', 'rain', 'windy']
        return {'cond': random.choice(choices), 'temp_c': random.randint(-5, 35)}

class WeatherAdapter:
    def __init__(self, external_service):
        self.service = external_service

    def current_weather(self):
        data = self.service.get_current()
        return {'condition': data['cond'], 'temperature_celsius': data['temp_c']}
