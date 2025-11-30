from builder import SmartCityBuilder
from logger import Logger
from proxy import SecurityProxy
from adapter import WeatherAdapter, ExternalWeatherAPI


class SmartCityController:
    """
    Facade — barcha modullar bilan ishlashni soddalashtiradi.
    Singleton — tizimda faqat bitta markaziy boshqaruvchi bo‘ladi.
    """
    __instance = None

    def __init__(self):
        self.log = Logger.get_instance()

        # Builder orqali modullarni quramiz
        self.city = SmartCityBuilder()\
            .add_lighting()\
            .add_transport()\
            .add_security()\
            .add_energy()\
            .build()

        self.log.log("SmartCity tizimi ishga tushirildi!")

    @staticmethod
    def get_instance():
        if SmartCityController.__instance is None:
            SmartCityController.__instance = SmartCityController()
        return SmartCityController.__instance

    def run(self):
        """
        Konsol interfeysi
        """
        while True:
            print("""
=== SMART CITY ===
1) Ko‘cha yoritishi
2) Transport
3) Xavfsizlik
4) Energiya
5) Ob-havo (Adapter)
0) Chiqish
""")
            c = input("Tanlang: ")

            if c == "0": break
            if c == "1": self.city["lighting"].turn_on()
            if c == "2": self.city["transport"].add_bus()
            if c == "3":
                parol = input("Parol: ")
                SecurityProxy(self.city["security"]).monitor(parol)
            if c == "4":
                self.city["energy"].save(3)
                print(self.city["energy"].report())
            if c == "5":
                print(WeatherAdapter(ExternalWeatherAPI()).city_temp())
