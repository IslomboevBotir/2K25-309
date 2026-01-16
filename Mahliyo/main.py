"""
Console entry point:
- Builds a city via Builder, using an Abstract Factory profile.
- Attaches to Facade (controller) and reads simple commands.
"""

import sys

from core.factories.concrete_factories import EcoCityFactory, StandardCityFactory
from core.builders.city_builder import CityBuilder
from core.adapters.weather_adapter import ExternalWeatherClient, WeatherServiceAdapter
from core.controller import SmartCityController


def build_city(profile: str, name: str):
    if profile == "eco":
        factory = EcoCityFactory()
    else:
        factory = StandardCityFactory()

    weather_adapter = WeatherServiceAdapter(ExternalWeatherClient())
    builder = CityBuilder(factory).with_name(name).with_weather(weather_adapter)
    return builder.build()


def print_help():
    print("📖 Commands:")
    print("  1️⃣ 🏙 status")
    print("  2️⃣ 🚌 dispatch")
    print("  3️⃣ 💡 lights on")
    print("  4️⃣ 🌙 lights off")
    print("  5️⃣ 🎥 monitor <role>")
    print("  6️⃣ 🔋 energy")
    print("  7️⃣ ☀️ weather <zone>")
    print("  8️⃣ ❓ help")
    print("  9️⃣ 🚪 exit")


def main():
    profile = "eco"
    name = "Tashkent-SmartCity"

    if len(sys.argv) >= 2:
        profile = sys.argv[1]  # eco|standard
    if len(sys.argv) >= 3:
        name = sys.argv[2]

    city = build_city(profile, name)
    controller = SmartCityController()
    controller.attach_city(city)

    print(f"✅ Loaded {controller.status()}")
    print_help()

    while True:
        try:
            cmd = input("👉 ").strip()
        except EOFError:
            break

        # map numbers to commands
        if cmd == "1":
            cmd = "status"
        elif cmd == "2":
            cmd = "dispatch"
        elif cmd == "3":
            cmd = "lights on"
        elif cmd == "4":
            cmd = "lights off"
        elif cmd == "5":
            cmd = "monitor admin"  # default role if none given
        elif cmd == "6":
            cmd = "energy"
        elif cmd == "7":
            cmd = "weather central"
        elif cmd == "8":
            cmd = "help"
        elif cmd == "9":
            cmd = "exit"

        if cmd == "exit":
            print("👋 Goodbye.")
            break
        elif cmd == "help":
            print_help()
        elif cmd == "status":
            print(f"🏙 {controller.status()}")
        elif cmd == "dispatch":
            print(f"🚌 {controller.dispatch_transport()}")
        elif cmd == "lights on":
            print(f"💡 {controller.lights_on()}")
        elif cmd == "lights off":
            print(f"🌙 {controller.lights_off()}")
        elif cmd.startswith("monitor"):
            parts = cmd.split()
            role = parts[1] if len(parts) > 1 else "guest"
            print(f"🎥 {controller.security_monitor(role)}")
        elif cmd.startswith("weather"):
            parts = cmd.split()
            zone = parts[1] if len(parts) > 1 else "central"
            print(f"☀️ {controller.weather(zone)}")
        elif cmd == "energy":
            print(f"🔋 {controller.energy_report()}")
        else:
            print("❌ Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
