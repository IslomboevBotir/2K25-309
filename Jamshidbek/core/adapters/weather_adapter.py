import random


class ExternalWeatherService:
    """
    Simulated third-party service (different interface).
    We don't change it; we adapt it.
    """
    def fetch_weather(self, city: str) -> dict:
        return {
            "city": city,
            "temp_c": random.randint(-10, 45),
            "condition": random.choice(["sunny", "cloudy", "rainy", "windy"]),
        }


class WeatherProvider:
    """Target interface expected by our system."""
    def get_summary(self) -> str:
        raise NotImplementedError


class WeatherAdapter(WeatherProvider):
    """
    Adapter Pattern:
    Adapts ExternalWeatherService to WeatherProvider interface.
    """
    def __init__(self, external: ExternalWeatherService, city: str) -> None:
        self._external = external
        self._city = city

    def get_summary(self) -> str:
        data = self._external.fetch_weather(self._city)
        return f"Weather in {data['city']}: {data['temp_c']}°C, {data['condition']}"
