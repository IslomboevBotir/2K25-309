"""
Security Management Subsystem
"""

class SecuritySystem:
    def __init__(self):
        self.cameras = []
        self.alarm_active = False
    
    def add_camera(self, location):
        self.cameras.append({"location": location, "active": True})
    
    def activate_alarm(self):
        self.alarm_active = True
        return "🔒 Security: Alarm ACTIVATED"
    
    def deactivate_alarm(self):
        self.alarm_active = False
        return "🔒 Security: Alarm deactivated"
    
    def get_status(self):
        alarm_status = "ACTIVE" if self.alarm_active else "Standby"
        camera_count = len(self.cameras)
        return f"🔒 Security System: {camera_count} cameras | Alarm: {alarm_status}"