from typing import Dict


class ExternalWeatherClient:
    def fetch_conditions(self, zone: str) -> Dict[str, str]:
        # Simulated external service response
        return {
            "zone": zone,
            "temp_c": "7",
            "condition": "clear",
            "wind_kph": "12",
        }


class WeatherServiceAdapter:
    def __init__(self, client: ExternalWeatherClient):
        self.client = client

    def get_weather_summary(self, zone: str) -> str:
        data = self.client.fetch_conditions(zone)
        return (
            f"Weather in {data['zone']}: {data['temp_c']}°C, "
            f"{data['condition']}, wind {data['wind_kph']} kph"
        )
