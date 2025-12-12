"""
Adapter module.

Implements the Adapter design pattern to integrate an external weather
service with an interface that is convenient for the SmartCity system.
"""


class ExternalWeatherAPI:
    """
    Simulated external weather API with its own interface.
    """

    def fetch_data(self) -> dict:
        # Simulated external response format
        return {
            "temperature": 25,
            "units": "C",
            "description": "Sunny with light wind",
        }


class WeatherServiceAdapter:
    """
    Adapter that converts the ExternalWeatherAPI interface into
    a method suitable for our domain: get_weather_info() -> str.
    """

    def __init__(self):
        self._api = ExternalWeatherAPI()

    def get_weather_info(self) -> str:
        data = self._api.fetch_data()
        temp = data["temperature"]
        units = data["units"]
        desc = data["description"]
        return f"{temp}°{units}, {desc}"
