from typing import Protocol


class SecurityOps(Protocol):
    def monitor(self) -> str: 


class SecurityProxy:
    def __init__(self, security: SecurityOps):
        self._security = security

    def monitor(self, role: str) -> str:
        if role not in ("admin", "operator"):
            return "Access denied: insufficient role"
        return self._security.monitor()
