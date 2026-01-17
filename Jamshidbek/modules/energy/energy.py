class EnergySystem:
    """Energy saving and monitoring subsystem."""
    def __init__(self) -> None:
        self._consumption_kw = 120
        self._saving_mode = False

    def toggle_saving_mode(self) -> str:
        self._saving_mode = not self._saving_mode
        if self._saving_mode:
            self._consumption_kw = max(50, self._consumption_kw - 20)
            return "Energy: saving mode ON"
        self._consumption_kw += 10
        return "Energy: saving mode OFF"

    def status(self) -> str:
        return f"Energy status: consumption={self._consumption_kw} kW, saving_mode={self._saving_mode}"
