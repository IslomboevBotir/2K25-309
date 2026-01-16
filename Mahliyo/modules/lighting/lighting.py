from typing import List
from dataclasses import dataclass


@dataclass
class Light:
    kind: str
    power: int
    on: bool = False

    def toggle(self, state: bool) -> None:
        self.on = state

    def info(self) -> str:
        return f"{self.kind} ({self.power}W, {'on' if self.on else 'off'})"


class LightingManager:
    def __init__(self, profile: str):
        self.profile = profile
        self.lights: List[Light] = []

    def add_light(self, kind: str, power: int) -> None:
        self.lights.append(Light(kind=kind, power=power))

    def turn_on_all(self) -> str:
        for l in self.lights:
            l.toggle(True)
        return "Lights on: " + ", ".join(l.info() for l in self.lights)

    def turn_off_all(self) -> str:
        for l in self.lights:
            l.toggle(False)
        return "Lights off: " + ", ".join(l.info() for l in self.lights)
