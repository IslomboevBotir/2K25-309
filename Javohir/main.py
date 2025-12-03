from controller import SystemController
from adapter import WeatherAdapter
from proxy import SecurityProxy
from modules.energy import EnergySystem, EnergyMonitorDecorator
from modules.lighting import LightingSystem
from modules.transport import TransportSystem
from modules.security import SecuritySystem


def print_menu():
    print("\n=== SMART CITY ===")
    print("1. Barcha tizimlarni ishga tushirish")
    print("2. Ob-havo ma'lumoti")
    print("3. Energiya tizimi holati")
    print("4. Yoritish tizimini yoqish")
    print("5. Transport ma'lumotlari")
    print("6. Xavfsizlik skaneri")
    print("0. Chiqish")


def main():
    print("Rolni tanlang: admin yoki user")
    role = input(">>> ").strip().lower()
    proxy = SecurityProxy(role)

    # Tizimlarni yaratish
    controller = SystemController.get_instance()
    weather = WeatherAdapter()
    energy_monitor = EnergyMonitorDecorator(EnergySystem())
    lighting = LightingSystem()
    transport = TransportSystem()
    security = SecuritySystem()

    while True:
        print_menu()
        choice = input("Tanlov: ").strip()

        if choice == "1":
            proxy.execute(controller.start_city)

        elif choice == "2":
            proxy.execute(lambda: print(f"Ob-havo: {weather.get_temperature()}°C"))

        elif choice == "3":
            proxy.execute(energy_monitor.report)

        elif choice == "4":
            proxy.execute(lighting.turn_on)

        elif choice == "5":
            proxy.execute(transport.show_routes)

        elif choice == "6":
            proxy.execute(security.scan)

        elif choice == "0":
            print("Dastur tugadi.")
            break
        else:
            print("Noto‘g‘ri tanlov!")


if __name__ == "__main__":
    main()
