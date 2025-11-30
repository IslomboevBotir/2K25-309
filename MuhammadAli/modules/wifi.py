import random

class WiFiManager:
    def display_status(self):
        points = random.randint(300, 450)
        speed = random.randint(70, 150)
        print(f"\nUmumiy Wi-Fi tarmoqlari: {points} ta nuqta faol")
        print(f"O'rtacha tezlik: {speed} Mbit/s")
