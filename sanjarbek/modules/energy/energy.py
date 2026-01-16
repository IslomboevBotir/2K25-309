# modules/energy/energy.py

class EnergySystem:
    """
    Energy subsystem (domain module).
    Purpose:
    - Track base energy consumption (kW)
    - Enable/disable energy saving mode
    - React to environment data (e.g., weather info)

    This file is business logic only (pattern-free).
    Adapter/Facade will connect external weather updates to this subsystem.
    """

    def __init__(self, base_consumption_kw: int = 120):
        self.base_consumption_kw = base_consumption_kw
        self.saving_mode: bool = False

        # Keep last known environment info as simple text (from Adapter later)
        self.last_weather_info: str = "Unknown"

    def enable_saving_mode(self) -> str:
        """
        Turn ON energy saving mode.
        """
        self.saving_mode = True
        return "Energy: saving mode ENABLED."

    def disable_saving_mode(self) -> str:
        """
        Turn OFF energy saving mode.
        """
        self.saving_mode = False
        return "Energy: saving mode DISABLED."

    def current_consumption(self) -> int:
        """
        Calculate current consumption based on saving mode.
        Example rule:
        - Normal: base consumption
        - Saving mode: 25% reduction
        """
        if self.saving_mode:
            return int(self.base_consumption_kw * 0.75)
        return self.base_consumption_kw

    def update_environment(self, weather_info: str) -> str:
        """
        Update energy behavior based on environment data.
        In real life it would parse structured data.
        Here we keep it simple: store string from Adapter.

        Example rule:
        - If weather mentions 'cold' or negative temperature -> consumption can increase
        - But since our adapter returns text like: Weather(temp=10C, condition=cloudy)
          we only store it for report now (extendable).
        """
        self.last_weather_info = weather_info
        return f"Energy: environment updated -> {weather_info}"

    def status(self) -> str:
        """
        Return a human-readable status for console/report.
        """
        mode = "ON" if self.saving_mode else "OFF"
        return (
            f"Energy: base={self.base_consumption_kw}kW, "
            f"current={self.current_consumption()}kW, "
            f"saving_mode={mode}, "
            f"weather={self.last_weather_info}"
        )
