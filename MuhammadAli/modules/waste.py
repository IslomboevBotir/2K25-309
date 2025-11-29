import random

class WasteManagement:
    def __init__(self):
        self.bins = {
            "Markaz": random.randint(20, 70),
            "Chorsu": random.randint(20, 85),
            "Olmazor": random.randint(91, 99),
            "Yunusobod": random.randint(10, 80)
        }

    def check_bins(self, report=False):
        if not report:
            print("\nCHIQINDI TIZIMI")
        for name, level in self.bins.items():
            if level > 90:
                print(f"   {name}: {level}% → TO'LIQ → Mashina yuborildi!")
            else:
                print(f"   {name}: {level}% → NORMAL")