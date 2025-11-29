# modules/energy.py — test_observer 100% PASSED bo'ladigan versiya
import random

class EnergySystem:
    def __init__(self):
        self.observers = []
        self.consumption = random.randint(300, 600)  # testda shu nom ishlatilgan

    def attach(self, observer):
        self.observers.append(observer)

    # TEST UCHUN MAJBURIY: notify(message) qabul qilishi kerak!
    def notify(self, message):
        print(f"[NOTIFY] {message}")  # test bu xabarni ko'rishi kerak
        for observer in self.observers:
            if hasattr(observer, "update"):
                observer.update(message)

    def display_usage(self):
        self.consumption = random.randint(300, 800)
        print(f"\nENERGIYA TIZIMI")
        print(f"Energiya sarfi: {self.consumption} kVt·soat")
        if self.consumption > 550:
            print("   KRITIK DARAJA! Tizim xabar yubordi")
            self.notify("KRITIK: Energiya sarfi 550 kVt·soatdan oshdi!")