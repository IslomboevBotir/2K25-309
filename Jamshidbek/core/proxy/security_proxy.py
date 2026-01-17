from Jamshidbek.modules.security.security import SecuritySystem


class SecurityProxy:
    """
    Proxy Pattern:
    Controls access to SecuritySystem based on role.
    - admin can arm/disarm
    - guest can only add/view alerts
    """
    def __init__(self, real: SecuritySystem, role: str) -> None:
        self._real = real
        self._role = role if role in ("admin", "guest") else "guest"

    def set_role(self, role: str) -> None:
        role = (role or "").strip().lower()
        self._role = role if role in ("admin", "guest") else "guest"

    def arm(self) -> str:
        if self._role != "admin":
            return "Security: access denied (admin required)"
        return self._real.arm()

    def disarm(self) -> str:
        if self._role != "admin":
            return "Security: access denied (admin required)"
        return self._real.disarm()

    def add_alert(self, message: str) -> str:
        return self._real.add_alert(message)

    def recent_alerts(self, limit: int = 5) -> str:
        return self._real.recent_alerts(limit)

    def status(self) -> str:
        return self._real.status() + f" (role={self._role})"
