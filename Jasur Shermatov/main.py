from core.controller import Controller

def show_menu():
    print("""
Select action by number:
------------------------------------------------
1. 🏙 Show system status
2. 💡 Turn ON all city lights
3. 🌙 Turn OFF all city lights
4. 🚦 Start traffic system
5. 🚨 Trigger threat alarm
6. ✅ Reset security alarm
7. ⚡ Check energy consumption
8. 🌱 Enable energy optimization
9. ❗ Disable energy optimization
10. 🌦 Simulate weather
0. 👋 Exit
------------------------------------------------
""")

def main():
    controller = Controller()

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        print()  # spacer line

        if choice == "1":
            controller.system_status()

        elif choice == "2":
            controller.toggle_city_lights(True)

        elif choice == "3":
            controller.toggle_city_lights(False)

        elif choice == "4":
            controller.start_traffic_system()

        elif choice == "5":
            threat = input("Enter threat name: ")
            controller.detect_threat(threat)

        elif choice == "6":
            controller.security.reset_alarm()

        elif choice == "7":
            controller.monitor_energy()

        elif choice == "8":
            controller.energy.optimize()

        elif choice == "9":
            controller.energy.disable_optimization()

        elif choice == "10":
            controller.simulate_weather()

        elif choice == "0":
            print("👋 SmartCity System shutting down... Bye!")
            break

        else:
            print("❌ Invalid option, please try again!")

        print()  # end spacer

if __name__ == "__main__":
    main()
