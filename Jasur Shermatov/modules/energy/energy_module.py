import random

class EnergyModule:
    def __init__(self):
        self.energy_usage = 0.0  # kWh
        self.optimized = True

    def monitor(self):
        self.energy_usage = round(random.uniform(120.5, 560.9), 2)
        print(f"⚡ Current city energy consumption: {self.energy_usage} kWh")

    def optimize(self):
        self.optimized = True
        print("🌱 Energy usage optimization enabled ✅")

    def disable_optimization(self):
        self.optimized = False
        print("⚠️ Energy usage optimization disabled ❌")

    def status(self):
        opt_state = "Enabled ✅" if self.optimized else "Disabled ❌"

        print("\n--- ⚡ CITY ENERGY STATUS ---")
        print(f"Optimization: {opt_state}")
        print(f"Usage: {self.energy_usage} kWh (last checked)")
        print("-----------------------------\n")
