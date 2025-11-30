class ExternalWeatherAPI:
    """
    Tashqi ob-havo servisi (oddiy ko‘rinish)
    """
    def temperature(self):
        return 14


class WeatherAdapter:
    """
    Adapter — tashqi API natijasini bizga qulay formatga moslaydi
    """
    def __init__(self, api: ExternalWeatherAPI):
        self.api = api

    def city_temp(self):
        return f"Shahardagi harorat: {self.api.temperature()}°C"
