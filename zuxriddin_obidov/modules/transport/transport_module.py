class Vehicle:
    def __init__(self, vehicle_id: int, name: str):
        self.id = vehicle_id
        self.name = name
        self.status_v = "unknown"

    def run(self):
        print(f"🚗 Vehicle {self.id} ({self.name}) → Running 🟢")
        self.status_v = "running"

    def stop(self):
        print(f"🚗 Vehicle {self.id} ({self.name}) → Stopped ❌")
        self.status_v = "stopped"

    def status(self):
        print(f"🚗 Vehicle {self.id} ({self.name}) → ready")
        return self.status_v

class Transports:
    def __init__(self, transports_name: str):
        self.name = transports_name
        self.vehicles: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def run_all(self):
        print(f"\n🚦 Transports '{self.name}' → starting all vehicles")
        for v in self.vehicles:
            v.run()

    def stop_all(self):
        print(f"\n🛑 Transports '{self.name}' → stopping all vehicles")
        for v in self.vehicles:
            v.stop()

    def status(self):
        print(f"\n🚌 Transports Status: {self.name}")
        for v in self.vehicles:
            v.status()

class TransportModule:
    def __init__(self):
        self.transports = Transports("City Transports")
        self.transports.add_vehicle(Vehicle(1, "Bus"))
        self.transports.add_vehicle(Vehicle(2, "Taxi"))
        self.schedule = None

    def start(self):
        print("🚦 Transport Module: ACTIVATED")
        self.transports.run_all()

    def stop(self):
        print("🛑 Transport Module: DEACTIVATED")
        self.transports.stop_all()

    def set_schedule(self, schedule):
        self.schedule = schedule

    def status(self):
        self.transports.status()
