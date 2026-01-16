
# Asosiy dastur fayli (main.py)

from core.controller import SmartCityController
from core.factories.city_factory import BasicCityFactory, PremiumCityFactory
from core.proxy.security_proxy import AccessDeniedError



# Shahar konfiguratsiyasini tanlash funksiyasi
def choose_factory() -> object:
    print("=== Aqlli Shahar Tizimi ===")
    print("Shahar turini tanlang:")
    print("1) Oddiy")
    print("2) Premium")

    choice = input("Tanlang (1/2): ").strip()
    if choice == "2":
        return PremiumCityFactory()
    return BasicCityFactory()



# Tizim holatini chiroyli chiqarish funksiyasi
def print_status_lines(lines: list[str]) -> None:
    print("\n--- TIZIM HOLATI ---")
    for line in lines:
        print(line)


def main():
    # Dastur ishga tushirilganda shahar konfiguratsiyasini tanlaymiz va boshqaruvchini yaratamiz
    factory = choose_factory()
    controller = SmartCityController(factory=factory)

    while True:
        print("\n--- MENYU ---")
        print("1) Holatni ko'rsatish")
        print("2) Transport: avtobus yuborish")
        print("3) Yoritish: yorqinlikni o'zgartirish")
        print("4) Energiya: tejash rejimini yoqish")
        print("5) Energiya: tejash rejimini o'chirish")
        print("6) Xavfsizlik: QULFLASH (faqat admin)")
        print("7) Xavfsizlik: QULFDAN CHIQARISH (faqat admin)")
        print("8) Ob-havoni yangilash (Adapter)")
        print("9) Hisobot yaratish (Builder)")
        print("0) Exit")

        cmd = input("Your choice: ").strip()

        if cmd == "1":
            print_status_lines(controller.show_status())

        elif cmd == "2":
            route = input("Route name (e.g., A1): ").strip()
            print(controller.transport_dispatch(route))

        elif cmd == "3":
            level = input("Brightness (0-100): ").strip()
            print(controller.lighting_set_brightness(level))

        elif cmd == "4":
            print(controller.energy_enable_saving_mode())

        elif cmd == "5":
            print(controller.energy_disable_saving_mode())

        elif cmd == "6":
            token = input("Enter admin token: ").strip()
            try:
                print(controller.security_arm(token))
            except AccessDeniedError as e:
                print(f"Security: {e}")

        elif cmd == "7":
            token = input("Enter admin token: ").strip()
            try:
                print(controller.security_disarm(token))
            except AccessDeniedError as e:
                print(f"Security: {e}")

        elif cmd == "8":
            print(controller.sync_weather())

        elif cmd == "9":
            print("\n=== REPORT ===")
            print(controller.generate_report())

        elif cmd == "0":
            print("Bye!")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
