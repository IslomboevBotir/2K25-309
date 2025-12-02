from core.adapter.weather_adapter import WeatherAdapter, ExternalWeatherAPI


# --- Component Interface ---
class StreetLightComponent:
    def operation(self):
        return "Basic street light is ON."


# --- Concrete Component ---
class StandardStreetLight(StreetLightComponent):
    def operation(self):
        return "Standard street light is brightly lit."


# --- Base Decorator ---
class LightDecorator(StreetLightComponent):
    """
    DESIGN PATTERN: DECORATOR
    Allows dynamic attachment of additional responsibilities to an object
    (a StreetLightComponent) without altering its structure.
    """

    def __init__(self, component: StreetLightComponent):
        self._component = component

    def operation(self):
        return self._component.operation()


# --- Concrete Decorator ---
class DimmableLightDecorator(LightDecorator):
    def operation(self):
        # Adding new behavior before/after the wrapped object's behavior
        base_op = self._component.operation()
        return f"{base_op} | Function: Dimming Light by 20% to save energy."


# --- Lighting Manager (uses the Adapter) ---
class LightingManager:
    def __init__(self):
        self.weather_service = WeatherAdapter(ExternalWeatherAPI())
        self.main_light = DimmableLightDecorator(StandardStreetLight())  # Decorated light

    def optimize_lighting_for_weather(self):
        weather = self.weather_service.get_current_conditions()
        print(f"Lighting System: Using Adapter to read weather: {weather}")

        # Logic using the Decorated light
        if "Cloudy" in weather:
            print(f"Lighting Logic: Weather is poor, turning lights to full brightness.")
            return StandardStreetLight().operation()
        else:
            return self.main_light.operation()

    def get_status(self):
        return "Operational"