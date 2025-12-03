class ExternalWeatherAPI:
    def temperature(self):
        return 16  # misol uchun

class WeatherAdapter:
    def __init__(self, api=None):
        self.api = api or ExternalWeatherAPI()

    def get_temperature(self):
        return self.api.temperature()

    def city_temp(self):
        return f"Shahardagi harorat: {self.api.temperature()}°C"
