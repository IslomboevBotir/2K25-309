# core/adapters/weather_adapter.py

import random


class ExternalWeatherAPI:
    """
    Tashqi (3-tomon) ob-havo xizmatining soddalashtirilgan modeli.

    MUHIM:
    Bu xizmat o‘ziga xos interfeys va formatga ega.
    Bizning Aqlli Shahar tizimi to‘g‘ridan-to‘g‘ri unga bog‘liq bo‘lishini xohlamaydi.
    """

    def fetch_weather(self) -> dict:
        # Tashqi API o‘z strukturasi bilan lug‘at (dict) qaytaradi
        return {
            "temp_c": random.randint(-10, 40),
            "condition": random.choice(["sunny", "cloudy", "rainy", "snowy"]),
        }


class WeatherServiceAdapter:
    """
    Pattern: Adapter (Struktural)

    Maqsad:
    Tashqi ob-havo API ni ichki, qulay formatga moslashtirish.

    ExternalWeatherAPI -> dict qaytaradi
    Aqlli shahar tizimi esa oddiy matn yoki yagona obyekt xohlaydi

    Keyinchalik ExternalWeatherAPI ni haqiqiy API ga almashtirsangiz ham,
    controller kodini o‘zgartirish shart emas.
    """

    def __init__(self):
        self._api = ExternalWeatherAPI()

    def get_current_weather(self) -> str:
        raw = self._api.fetch_weather()

        # Convert ("adapt") to our internal domain-friendly format
        return f"Weather(temp={raw['temp_c']}C, condition={raw['condition']})"
