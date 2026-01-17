class LightingSystem:
    """Lighting subsystem."""
    def __init__(self) -> None:
        self._is_on = False
        self._brightness = 50  # 0..100

    def turn_on(self) -> str:
        self._is_on = True
        return "Lighting: ON"

    def turn_off(self) -> str:
        self._is_on = False
        return "Lighting: OFF"

    def set_brightness(self, value: int) -> str:
        value = max(0, min(100, int(value)))
        self._brightness = value
        return f"Lighting: brightness set to {self._brightness}%"

    def status(self) -> str:
        return f"Lighting status: on={self._is_on}, brightness={self._brightness}%"


class EcoLightingDecorator(LightingSystem):
    """
    Decorator Pattern:
    Adds eco behavior without changing LightingSystem.
    Caps brightness to save energy.
    """
    def __init__(self, base: LightingSystem, max_brightness: int = 60) -> None:
        self._base = base
        self._cap = max(10, min(100, int(max_brightness)))

    def turn_on(self) -> str:
        return self._base.turn_on()

    def turn_off(self) -> str:
        return self._base.turn_off()

    def set_brightness(self, value: int) -> str:
        if int(value) > self._cap:
            value = self._cap
            msg = self._base.set_brightness(value)
            return msg + f" (Eco cap applied: {self._cap}%)"
        return self._base.set_brightness(value)

    def status(self) -> str:
        return self._base.status() + f" (eco_cap={self._cap}%)"
