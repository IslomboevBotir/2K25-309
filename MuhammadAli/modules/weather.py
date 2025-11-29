# modules/weather.py (to'liq va testdan o'tadigan versiya)
import random

class WeatherSystem:
    def __init__(self):
        self.conditions = ["quyoshli", "bulutli", "yomg'irli", "shamolli", "qorli"]

    def get_current_weather(self):
        condition = random.choice(self.conditions)
        temp = random.randint(10, 35)
        return {"condition": condition, "temp": temp}

    def display_current(self):
        data = self.get_current_weather()
        print(f"\nOB-HAVO")
        print(f"Ob-havo: {data['condition'].title()}, {data['temp']}°C")