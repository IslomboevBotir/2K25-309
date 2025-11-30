from core.controller import SmartCityController

def main():
    # Singleton + Facade
    city = SmartCityController()

    # Subscribe observers
    city.event_manager.subscribe(city.security)
    city.event_manager.subscribe(city.energy.meter.meter)  # nested observer

    # Start system
    city.start_city()

    # Simulate events
    city.simulate_event("peak_hour")
    city.simulate_event("intrusion")

    # Shutdown
    city.stop_city()

if __name__ == "__main__":
    main()