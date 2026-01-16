from typing import List
from dataclasses import dataclass


@dataclass
class Camera:
    resolution: str

    def stream_info(self) -> str:
        return f"Camera[{self.resolution}] streaming"


class SecurityManager:

    def __init__(self, profile: str):
        self.profile = profile
        self.cameras: List[Camera] = []

    def add_camera(self, resolution: str) -> None:
        self.cameras.append(Camera(resolution=resolution))

    def monitor(self) -> str:
        if not self.cameras:
            return "No cameras online."
        return "Monitoring: " + "; ".join(c.stream_info() for c in self.cameras)
