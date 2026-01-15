class ExternalWeatherAPI:
    def fetch_data(self) -> dict:
        # Simulated external response format
        return {
            "temperature": 25,
            "units": "C",
            "description": "Sunny with light wind",
        }


class WeatherServiceAdapter:
    def __init__(self):
        self._api = ExternalWeatherAPI()

    def get_weather_info(self) -> str:
        data = self._api.fetch_data()
        temp = data["temperature"]
        units = data["units"]
        desc = data["description"]
        return f"{temp}°{units}, {desc}"
