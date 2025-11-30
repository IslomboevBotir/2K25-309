import os
os.environ["SMARTCITY_SILENT"] = "1"

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
            if cmd.lower() == "camera":
                pwd = input("Xavfsizlik parolini kiriting: ").strip()
                if pwd == "smart2025":
                    controller.access_security_camera(pwd)
                    continue
                else:
                    print("PAROL XATO! Kirish rad etildi")
                    continue
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
