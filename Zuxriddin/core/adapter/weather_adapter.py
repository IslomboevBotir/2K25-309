# core/adapters/weather_adapter.py

# The third-party service with an incompatible interface (the Adaptee)
class ExternalWeatherAPI:
    def get_meteorological_data_json(self):
        """Returns data in a proprietary json format."""
        return {"pressure": 750, "visibility_km":0.7, "condition":"Cloudy"}


# The Target interface the client (City Controller) expects
class WeatherService:
    def get_current_conditions(self):
        pass


class WeatherAdapter(WeatherService):
    """
    DESIGN PATTERN: ADAPTER
    Translates the incompatible interface of ExternalWeatherAPI into the
    WeatherService interface that the client code can use.
    """

    def __init__(self, external_api: ExternalWeatherAPI):
        self._external_api = external_api

    def get_current_conditions(self):
        # Translate the proprietary data format
        data = self._external_api.get_meteorological_data_json()

        pressure = data["pressure"]
        visibility_m = int(data["visibility_km"] * 1000)  # Convert factor to meters
        condition = data["condition"]

        return f"Pressure: {pressure}hPa, Visibility: {visibility_m}m, Conditions: {condition}"