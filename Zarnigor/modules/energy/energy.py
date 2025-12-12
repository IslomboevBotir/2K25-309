"""
Energy subsystem of SmartCity.

This version is expanded to match a more detailed, interactive style.
Includes:
- Randomized energy monitoring
- Optimization toggles
- Rich console output
- Clear status reporting
"""

import random


class EnergySystem:
    """
    Represents the city's energy management subsystem.
    Tracks energy usage, optimization state, and provides monitoring tools.
    """

    def __init__(self):
        # kWh usage (updated dynamically)
        self.energy_usage = 0.0

        # Whether optimization mode is active
        self.optimized = True

        # Historical / static info
        self.peak_hour = "18:00"
        self.renewable_share = 42  # percent

    def monitor(self):
        """
        Simulates real-time energy monitoring.
        Generates a random usage value to mimic sensor readings.
        """
        self.energy_usage = round(random.uniform(120.5, 560.9), 2)
        print(f"⚡ Current city energy consumption: {self.energy_usage} kWh")

    def optimize(self):
        """
        Enables energy optimization mode.
        """
        self.optimized = True
        print("🌱 Energy usage optimization enabled ✅")

    def disable_optimization(self):
        """
        Disables energy optimization mode.
        """
        self.optimized = False
        print("⚠️ Energy usage optimization disabled ❌")

    def get_status(self) -> str:
        """
        Returns a summary string for the SmartCityController (Facade).
        """
        opt_state = "Enabled ✅" if self.optimized else "Disabled ❌"
        return (
            f"Energy: {self.energy_usage} kWh (last check), "
            f"Optimization: {opt_state}, "
            f"Renewables: {self.renewable_share}%, "
            f"Peak hour: {self.peak_hour}."
        )

    def status(self):
        """
        Prints a detailed, formatted energy status report.
        """
        opt_state = "Enabled ✅" if self.optimized else "Disabled ❌"

        print("\n--- ⚡ CITY ENERGY STATUS ---")
        print(f"Optimization: {opt_state}")
        print(f"Usage: {self.energy_usage} kWh (last checked)")
        print(f"Renewable share: {self.renewable_share}%")
        print(f"Peak hour: {self.peak_hour}")
        print("-----------------------------\n")
