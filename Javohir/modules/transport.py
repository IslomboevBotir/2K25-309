from logger import Logger

class TransportSystem:
    """
    Ommaviy transportni boshqarish
    """
    def __init__(self):
        self.bus_count = 0
        self.log = Logger.get_instance()

    def add_bus(self):
        self.bus_count += 1
        self.log.log(f"Yangi avtobus qo‘shildi. Jami: {self.bus_count} ta")
