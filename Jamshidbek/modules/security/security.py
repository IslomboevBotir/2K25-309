class SecuritySystem:
    def __init__(self) -> None:
        self._armed = False
        self._alerts = []

    def arm(self) -> str:
        self._armed = True
        return "Security: ARMED"

    def disarm(self) -> str:
        self._armed = False
        return "Security: DISARMED"

    def add_alert(self, message: str) -> str:
        message = (message or "").strip() or "Unknown alert"
        self._alerts.append(message)
        return f"Security: alert added ({message})"

    def recent_alerts(self, limit: int = 5) -> str:
        items = self._alerts[-limit:]
        if not items:
            return "Security alerts:\n- none"
        return "Security alerts:\n" + "\n".join(f"- {x}" for x in items)

    # ✅ ADD THIS
    def status(self) -> str:
        return f"Security status: armed={self._armed}, alerts={len(self._alerts)}"
