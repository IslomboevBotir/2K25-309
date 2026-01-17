class TransportSystem:
    """Transportation management subsystem."""
    def __init__(self) -> None:
        self._traffic_level = 3  # 1..5
        self._signals_auto = True

    def set_traffic_level(self, level: int) -> str:
        self._traffic_level = max(1, min(5, int(level)))
        return f"Transport: traffic level set to {self._traffic_level}/5"

    def toggle_signals_mode(self) -> str:
        self._signals_auto = not self._signals_auto
        return f"Transport: signals auto={self._signals_auto}"

    def optimize_routes(self) -> str:
        if self._traffic_level >= 4:
            return "Transport: rerouting applied (high traffic)."
        return "Transport: routes normal (no changes)."

    def status(self) -> str:
        return f"Transport status: traffic={self._traffic_level}/5, signals_auto={self._signals_auto}"
