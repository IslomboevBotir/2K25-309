from dataclasses import dataclass


@dataclass
class Vehicle:
    kind: str
    capacity: int

    def info(self) -> str:
        return f"{self.kind} (cap {self.capacity})"


class VehicleFactory:
    @staticmethod
    def create(kind: str, capacity: int) -> Vehicle:
        # In a real app, you'd map kinds to concrete classes
        return Vehicle(kind=kind, capacity=capacity)