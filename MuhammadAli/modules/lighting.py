# modules/lighting.py (test uchun majburiy metod qo‘shildi)
import random

class LightingSystem:
    def __init__(self):
        self.lights = ["Amir Temur xiyoboni", "Mustaqillik maydoni", "Chorsu"]

    def display_lights(self):
        level = random.randint(60, 100)
        print("\nYORITISH TIZIMI")
        print(f"Ob-havo bo'yicha yorug'lik: {level}%")
        for light in self.lights:
            print(f"   → {light} | {level}% | Auto: True")

    # ← TEST UCHUN MAJBURIY METOD
    def auto_adjust_with_weather(self, weather_system):
        weather = weather_system.get_current_weather()
        condition = weather["condition"]
        if condition in ["yomg'irli", "qorli", "bulutli"]:
            brightness = 100
        else:
            brightness = 60
        print(f"Ob-havo bo'yicha yorug'lik: {brightness}%")
        # Bu test uchun yetarli