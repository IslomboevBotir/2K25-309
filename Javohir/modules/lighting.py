from logger import Logger

class LightingSystem:
    """
    Shahar ko‘cha chiroqlarini boshqarish
    """
    def __init__(self):
        self.state = False
        self.log = Logger.get_instance()

    def turn_on(self):
        self.state = True
        self.log.log("Ko‘cha chiroqlari yoqildi.")

    def turn_off(self):
        self.state = False
        self.log.log("Ko‘cha chiroqlari o‘chirildi.")
