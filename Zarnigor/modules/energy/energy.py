import random


class EnergySystem:
    def __init__(self):
        self.energy_usage = 0.0
        self.optimized = True
        self.peak_hour = "18:00"
        self.renewable_share = 42

    def monitor(self):
        self.energy_usage = round(random.uniform(120.5, 560.9), 2)
        print(f"⚡ Current city energy consumption: {self.energy_usage} kWh")

    def optimize(self):
        self.optimized = True
        print("🌱 Energy usage optimization enabled ✅")

    def disable_optimization(self):
        self.optimized = False
        print("⚠️ Energy usage optimization disabled ❌")

    def get_status(self) -> str:
        opt_state = "Enabled ✅" if self.optimized else "Disabled ❌"
        return (
            f"Energy: {self.energy_usage} kWh (last check), "
            f"Optimization: {opt_state}, "
            f"Renewables: {self.renewable_share}%, "
            f"Peak hour: {self.peak_hour}."
        )

    def status(self):
        opt_state = "Enabled ✅" if self.optimized else "Disabled ❌"

        print("\n--- ⚡ CITY ENERGY STATUS ---")
        print(f"Optimization: {opt_state}")
        print(f"Usage: {self.energy_usage} kWh (last checked)")
        print(f"Renewable share: {self.renewable_share}%")
        print(f"Peak hour: {self.peak_hour}")
        print("-----------------------------\n")
