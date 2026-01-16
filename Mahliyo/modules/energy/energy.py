from typing import List
from dataclasses import dataclass


@dataclass
class Meter:
    location: str

    def read(self) -> str:
        # Simulated reading
        return f"{self.location}: 12.4 kWh"


class EnergyManager:

    def __init__(self, profile: str):
        self.profile = profile
        self.meters: List[Meter] = []

    def add_meter(self, location: str) -> None:
        self.meters.append(Meter(location=location))

    def report(self) -> str:
        if not self.meters:
            return "No meters installed."
        return "Energy report: " + " | ".join(m.read() for m in self.meters)
