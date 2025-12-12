"""
Proxy module.

Implements the Proxy design pattern to control access to subsystems
like SecuritySystem and LightingSystem.
"""


class SecurityProxy:
    """
    Proxy for SecuritySystem. It allows only 'admin' users to
    access detailed security logs, while regular users receive
    an access denied message.
    """

    def __init__(self, real_security_system):
        self._real_security_system = real_security_system

    def access(self, role: str) -> str:
        role = role.strip().lower()
        if role == "admin":
            return (
                "[ADMIN ACCESS GRANTED]\n"
                + self._real_security_system.get_detailed_log()
            )
        else:
            return "[ACCESS DENIED] Only admin can access detailed security information."


class LightingProxy:
    """
    Proxy for LightingSystem.
    Only admin can turn lights on/off.
    Everyone can view status.
    """

    def __init__(self, real_lighting_system):
        self._real = real_lighting_system

    def turn_all_on(self, role: str):
        role = role.strip().lower()
        if role == "admin":
            self._real.turn_all_on()
        else:
            print("❌ ACCESS DENIED: Only admin can turn on city lights.")

    def turn_all_off(self, role: str):
        role = role.strip().lower()
        if role == "admin":
            self._real.turn_all_off()
        else:
            print("❌ ACCESS DENIED: Only admin can turn off city lights.")

    def status(self):
        return self._real.get_status()
