
from typing import List
from .vehicles import VehicleFactory, Vehicle


class TransportManager:
    """
    Transport subsystem manager.
    - Uses a factory method to add different vehicles by kind.
    """
    def __init__(self, profile: str):
        self.profile = profile
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, kind: str, capacity: int) -> None:
        self.vehicles.append(VehicleFactory.create(kind, capacity))

    def dispatch(self) -> str:
        if not self.vehicles:
            return "No vehicles available."
        return "Dispatching: " + ", ".join(v.info() for v in self.vehicles)
