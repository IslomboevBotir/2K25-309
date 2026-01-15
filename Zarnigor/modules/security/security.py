"""
Security subsystem of SmartCity.

This expanded version matches a more expressive, feature-rich style.
Includes:
- Camera monitoring
- Alarm triggering/resetting
- Threat reporting
- Detailed status panel
- Compatibility with Proxy for admin access
"""


class SecuritySystem:
    """
    Represents the city's security infrastructure.
    Tracks camera activity, alarm state, and threat alerts.
    """

    def __init__(self):
        # Cameras are active by default
        self.cameras_active = True

        # Alarm state
        self.alarm_triggered = False

        # Last detected threat (if any)
        self.last_threat = "None"

        # Number of cameras in the city
        self.total_cameras = 120

    def trigger_alarm(self, threat: str):
        """
        Activates the alarm and logs the detected threat.
        """
        self.alarm_triggered = True
        self.last_threat = threat.upper()
        print(f"🚨 SECURITY ALERT! Threat detected: {self.last_threat}!")

    def reset_alarm(self):
        """
        Resets the alarm system.
        """
        self.alarm_triggered = False
        self.last_threat = "None"
        print("✅ Security alarm has been reset.")

    def disable_cameras(self):
        """
        Disables all city cameras.
        """
        self.cameras_active = False
        print("⚠️ All city cameras have been DISABLED ❌")

    def enable_cameras(self):
        """
        Enables all city cameras.
        """
        self.cameras_active = True
        print("🎥 All city cameras are now ACTIVE ✅")

    def status(self):
        """
        Prints a detailed, formatted security status report.
        """
        alarm_state = "TRIGGERED ❗" if self.alarm_triggered else "Normal ✅"
        cam_state = "Active 🎥" if self.cameras_active else "Disabled ❌"

        print("\n--- 🔐 CITY SECURITY STATUS ---")
        print(f"Cameras: {cam_state} ({self.total_cameras} units)")
        print(f"Alarm: {alarm_state}")
        print(f"Last Threat: {self.last_threat}")
        print("------------------------------\n")

    def get_status(self) -> str:
        """
        Returns a summary string for the SmartCityController (Facade).
        """
        alarm_state = "Triggered" if self.alarm_triggered else "Normal"
        cam_state = "Active" if self.cameras_active else "Disabled"

        return (
            f"Security: Cameras {cam_state}, "
            f"Alarm: {alarm_state}, "
            f"Last threat: {self.last_threat}."
        )

    def get_detailed_log(self) -> str:
        """
        Detailed information only accessible via Proxy for admin users.
        """
        return (
            "Security detailed log:\n"
            f"- Cameras active: {self.cameras_active}\n"
            f"- Total cameras: {self.total_cameras}\n"
            f"- Alarm triggered: {self.alarm_triggered}\n"
            f"- Last threat: {self.last_threat}\n"
        )
