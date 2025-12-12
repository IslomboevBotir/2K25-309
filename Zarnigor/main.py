"""
Entry point for SmartCity System.
Provides a console menu to interact with SmartCityController.
Uses dictionary-based dispatch instead of long if/elif chains.
"""

from core.controller import SmartCityController


def print_menu():
    print("\n================= 🏙 SMARTCITY CONTROL PANEL =================")
    print("1.  📊 Show full system status")
    print("2.  💡 Turn ON all city lights (admin only)")
    print("3.  🌙 Turn OFF all city lights (admin only)")
    print("4.  🚦 Start traffic system")
    print("5.  🚨 Trigger security alarm")
    print("6.  ✅ Reset security alarm")
    print("7.  ⚡ Monitor energy consumption")
    print("8.  🌱 Enable energy optimization")
    print("9.  ❗ Disable energy optimization")
    print("10. 🌦 Show weather information (Adapter)")
    print("0.  👋 Exit SmartCity")
    print("===============================================================")


def main():
    controller = SmartCityController()  # Facade + Singleton

    def ask_role():
        return input("Enter your role (admin/user): ").strip()

    def ask_threat():
        return input("Describe the threat (e.g., intruder, fire): ").strip()

    commands = {
        "1": controller.show_full_status,
        "2": lambda: controller.turn_city_lights_on(ask_role()),
        "3": lambda: controller.turn_city_lights_off(ask_role()),
        "4": controller.start_traffic,
        "5": lambda: controller.trigger_security_alarm(ask_threat()),
        "6": controller.reset_security_alarm,
        "7": controller.monitor_energy,
        "8": controller.enable_energy_optimization,
        "9": controller.disable_energy_optimization,
        "10": controller.show_weather,
        "0": lambda: print("👋 Exiting SmartCity System..."),
    }

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        action = commands.get(choice)

        if action:
            action()
            if choice == "0":
                break
        else:
            print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    main()
