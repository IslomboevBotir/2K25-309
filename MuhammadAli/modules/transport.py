import random

class TransportSystem:
    def __init__(self):
        self.buses = {
            "57": random.randint(1, 10),
            "21": random.randint(1, 15),
            "67": random.randint(2, 12)
        }

    def display_status(self, report=False):
        if not report:
            print("\nTRANSPORT TIZIMI")
        print("Svetoforlar: Yashil → Sariq → Qizil")
        for bus, minute in self.buses.items():
            print(f"• Avtobus {bus}: {minute} daqiqa")
        print("• Metro: 2 daqiqa")

    def set_traffic_mode(self, mode: str):
        mode = mode.lower().strip()
        if "rush" in mode or "pik" in mode:
            print("Trafik strategiyasi o'zgartirildi: RushHourTraffic")
            print("Svetofor strategiyasi ishga tushdi → Pik soat: 90s yashil")
        elif "night" in mode or "tunda" in mode:
            print("Trafik strategiyasi o'zgartirildi: NightTraffic")
            print("Svetofor strategiyasi ishga tushdi → Tunda: 30s yashil")
        else:
            print("Trafik strategiyasi o'zgartirildi: NormalTraffic")
            print("Svetofor strategiyasi ishga tushdi → Normal rejim: 60s yashil")
