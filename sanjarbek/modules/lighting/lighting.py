# modules/lighting/lighting.py

class LightingSystem:
    """
    Lighting subsystem (domain module).
    Purpose: Control city lighting zones and brightness level (0..100).

    This file stays pattern-free (business logic only).
    Patterns will be applied in core (Factory/Facade/etc.).
    """

    def __init__(self, zone_count: int = 3):
        if zone_count <= 0:
            zone_count = 1

        self.zone_count = zone_count
        # We keep a simple global brightness for the whole city (can be extended per-zone later)
        self.brightness: int = 50  # 0..100

    def set_brightness(self, level: int) -> str:
        """
        Set brightness level for city lighting.
        """
        try:
            level = int(level)
        except (TypeError, ValueError):
            return "Lighting: brightness must be an integer (0-100)."

        if level < 0 or level > 100:
            return "Lighting: brightness must be in range 0-100."

        self.brightness = level
        return f"Lighting: brightness set to {self.brightness}% for {self.zone_count} zones."

    def status(self) -> str:
        """
        Return a human-readable status for console/report.
        """
        return f"Lighting: zones={self.zone_count}, brightness={self.brightness}%"
