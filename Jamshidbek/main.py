import os
import sys

# Run as: python Jamshidbek/main.py
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(THIS_DIR)
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from Jamshidbek.core.builders.city_builder import CityConfigBuilder
from Jamshidbek.core.controller import SmartCityController


def menu() -> str:
    return """
=========================
 SmartCity Console System
=========================
1) Show city status
2) Set role (admin/guest)
3) Lighting: ON
4) Lighting: OFF
5) Lighting: Set brightness
6) Transport: Set traffic level (1..5)
7) Transport: Optimize routes
8) Transport: Toggle signals auto/manual
9) Security: ARM (admin)
10) Security: DISARM (admin)
11) Security: Add alert
12) Security: Show recent alerts
13) Energy: Toggle saving mode
0) Exit
"""


def main():
    cfg = (
        CityConfigBuilder()
        .city_name("SmartCity Lab")
        .zones_count(2)
        .eco_mode(True)
        .default_role("guest")
        .build()
    )

    controller = SmartCityController(cfg)

    while True:
        print(menu())
        choice = input("Choose: ").strip()

        try:
            if choice == "0":
                print("Bye!")
                break
            elif choice == "1":
                print(controller.city_status())
            elif choice == "2":
                role = input("Enter role (admin/guest): ").strip().lower()
                print(controller.set_role(role))
            elif choice == "3":
                print(controller.lighting_on())
            elif choice == "4":
                print(controller.lighting_off())
            elif choice == "5":
                v = int(input("Brightness (0..100): ").strip())
                print(controller.lighting_brightness(v))
            elif choice == "6":
                lvl = int(input("Traffic level (1..5): ").strip())
                print(controller.transport_set_traffic(lvl))
            elif choice == "7":
                print(controller.transport_optimize())
            elif choice == "8":
                print(controller.transport_toggle_signals())
            elif choice == "9":
                print(controller.security_arm())
            elif choice == "10":
                print(controller.security_disarm())
            elif choice == "11":
                msg = input("Alert message: ").strip()
                print(controller.security_add_alert(msg))
            elif choice == "12":
                print(controller.security_alerts())
            elif choice == "13":
                print(controller.energy_toggle())
            else:
                print("Invalid option!")
        except ValueError:
            print("Input error: enter number where required.")


if __name__ == "__main__":
    main()
