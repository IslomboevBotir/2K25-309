from logger import Logger

class EnergySystem:
    """
    Energiya tejash statistikasini yuritish
    """
    def __init__(self):
        self.savings = 0
        self.log = Logger.get_instance()

    def save(self, amount):
        self.savings += amount
        self.log.log(f"Energiya tejandi: {amount} kW")

    def report(self):
        return f"Jami tejangan energiya: {self.savings} kW"
