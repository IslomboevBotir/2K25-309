# modules/security/security.py

class SecuritySystem:
    """
    Security subsystem (domain module).
    Purpose:
    - Arm/disarm the city's security system
    - Track sensitivity level (low/medium/high)
    - Provide status for monitoring/report

    Note: Access control (who can arm/disarm) will be handled by Proxy in core layer.
    """

    def __init__(self, sensitivity: str = "medium"):
        self.sensitivity = self._normalize_sensitivity(sensitivity)
        self.armed: bool = False
        self.last_alert: str = "None"

    def _normalize_sensitivity(self, value: str) -> str:
        value = (value or "").strip().lower()
        if value not in {"low", "medium", "high"}:
            return "medium"
        return value

    def arm(self) -> str:
        """
        Arm the security system.
        (Proxy will protect this method in core layer.)
        """
        if self.armed:
            return "Security: system is already ARMED."
        self.armed = True
        return f"Security: system ARMED (sensitivity={self.sensitivity})."

    def disarm(self) -> str:
        """
        Disarm the security system.
        (Proxy can protect this too if you want.)
        """
        if not self.armed:
            return "Security: system is already DISARMED."
        self.armed = False
        return "Security: system DISARMED."

    def raise_alert(self, message: str) -> str:
        """
        Simulate an alert event (e.g., suspicious activity).
        """
        message = (message or "").strip()
        if not message:
            message = "Unknown alert"

        self.last_alert = message
        return f"Security: ALERT -> {self.last_alert}"

    def status(self) -> str:
        """
        Return a human-readable status for console/report.
        """
        state = "ARMED" if self.armed else "DISARMED"
        return (
            f"Security: state={state}, "
            f"sensitivity={self.sensitivity}, "
            f"last_alert={self.last_alert}"
        )
