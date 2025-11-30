from logger import Logger

class SecuritySystem:
    """
    Shahar kuzatuv kameralarini boshqarish
    """
    def __init__(self):
        self.cameras = 0
        self.log = Logger.get_instance()

    def add_camera(self):
        self.cameras += 1
        self.log.log(f"Kamera o‘rnatildi. Jami: {self.cameras} ta")

    def monitor(self):
        self.log.log("Shahar xavfsizligi monitoring qilinmoqda...")
