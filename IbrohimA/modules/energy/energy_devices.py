"""
Energy subsystem devices
"""


class EnergyMonitor:
    """Energy monitoring device"""
    
    def __init__(self, device_id: str, zone: str):
        self.device_id = device_id
        self.zone = zone
        self.is_monitoring = False
        self.power_consumption = 0  # kWh
    
    def start(self):
        """Start monitoring"""
        self.is_monitoring = True
        print(f"[ENERGY] {self.device_id} at {self.zone}: MONITORING START")
    
    def stop(self):
        """Stop monitoring"""
        self.is_monitoring = False
        print(f"[ENERGY] {self.device_id} at {self.zone}: MONITORING STOP")
    
    def status(self) -> dict:
        """Get energy monitor status"""
        return {
            'device_id': self.device_id,
            'zone': self.zone,
            'is_monitoring': self.is_monitoring,
            'power_consumption_kwh': self.power_consumption
        }
    
    def update_consumption(self, kwh: float):
        """Update power consumption reading"""
        self.power_consumption = kwh
        print(f"[ENERGY] {self.device_id}: Consumption updated to {kwh} kWh")
