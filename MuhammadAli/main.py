# main.py
import os
os.environ["SMARTCITY_SILENT"] = "1"  # Loglarni o'chirish uchun

from smartcity.controller import CityController
from smartcity.command_processor import CommandProcessor

def main():
    controller = CityController()
    processor = CommandProcessor()

    print("=" * 64)
    print(" SMARTCITY TIZIMI — TOSHKENT 2025")
    print("=" * 64)
    print("\nBO‘LIMLAR:")
    print("  transport | lighting | camera | energy | weather | waste | wifi | traffic rush | report | help | exit   ")
    print("-" * 103)

    while True:
        try:
            cmd = input("\n>>> ").strip()

            # Agar faqat "camera" yozsa — parol so‘raymiz
            if cmd.lower() == "camera":
                pwd = input("Xavfsizlik parolini kiriting: ").strip()
                if pwd == "smart2025":
                    controller.access_security_camera(pwd)  # To‘g‘ridan-to‘g‘ri chaqiramiz
                    continue
                else:
                    print("PAROL XATO! Kirish rad etildi")
                    continue

            # Boshqa buyruqlar processor orqali
            if cmd.lower() in ["exit", "chiqish", "quit", "0"]:
                print("\nSmartCity tizimi o‘chirildi. Xayr!")
                break

            if not processor.process(cmd, controller):
                break

        except (KeyboardInterrupt, EOFError):
            print("\n\nXayr!")
            break

if __name__ == "__main__":
    main()