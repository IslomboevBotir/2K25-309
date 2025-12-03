from logger import Logger

class EnergySystem:
    def __init__(self):
        self.savings = 0
        self.log = Logger.get_instance()

    def save(self, amount):
        self.savings += amount
        self.log.log(f"Energiya tejaldi: {amount} kW")

    def report(self):
        return f"Jami tejangan energiya: {self.savings} kW"

class EnergyMonitorDecorator:
    def __init__(self, energy_system):
        self.energy_system = energy_system

    def report(self):
        base = self.energy_system.report()
        return f"[Monitoring] {base} | Tizim barqaror"
