from core.event_manager import Observer

class EnergyMeter(Observer):
    def start_monitoring(self):
        print("⚡ Energy Meter: Monitoring started")
    def stop_monitoring(self):
        print("⚡ Energy Meter: Monitoring stopped")

    def update(self, event: str):
        if event == "peak_hour":
            print("⚠️ Peak energy usage detected!")

# Decorator
class SmartEnergyMeter:
    def __init__(self, meter: EnergyMeter):
        self.meter = meter

    def start_monitoring(self):
        print("🧠 Smart Energy System: AI optimization enabled")
        self.meter.start_monitoring()

    def stop_monitoring(self):
        self.meter.stop_monitoring()
        print("🧠 Smart Energy System: Saving usage report...")

class EnergyMeterSystem:
    def __init__(self):
        self.meter = SmartEnergyMeter(EnergyMeter())

    def start_monitoring(self):
        self.meter.start_monitoring()

    def stop_monitoring(self):
        self.meter.stop_monitoring()