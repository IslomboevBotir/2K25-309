class SecurityModule:
    def __init__(self):
        self.cameras_active = True
        self.alarm_triggered = False

    def trigger_alarm(self, threat: str):
        self.alarm_triggered = True
        print(f"🚨 SECURITY ALERT! Threat detected: {threat.upper()}!")

    def reset_alarm(self):
        self.alarm_triggered = False
        print("✅ Security alarm has been reset.")

    def status(self):
        alarm_state = "TRIGGERED ❗" if self.alarm_triggered else "Normal ✅"
        cam_state = "Active 🎥" if self.cameras_active else "Disabled ❌"

        print("\n--- 🔐 CITY SECURITY STATUS ---")
        print(f"Cameras: {cam_state}")
        print(f"Alarm: {alarm_state}")
        print("------------------------------\n")
