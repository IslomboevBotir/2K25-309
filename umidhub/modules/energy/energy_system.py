"""
Energy Monitoring Subsystem
"""

class EnergySystem:
    def __init__(self):
        self.total_consumption = 0
        self.devices = []
    
    def register_device(self, device_name, power_usage):
        self.devices.append({"name": device_name, "power": power_usage})
        self.total_consumption += power_usage
    
    def get_status(self):
        return f"⚡ Energy System: Total consumption {self.total_consumption} kW"
    
    def optimize_energy(self):
        reduction = self.total_consumption * 0.15
        return f"⚡ Energy optimized: Saved {reduction:.2f} kW"