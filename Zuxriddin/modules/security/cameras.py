from core.event_manager import Observer

# Legacy system
class OldCameraSystem:
    def enable_recording(self):
        print("🎥 Old Camera: Recording ON")
    def disable_recording(self):
        print("🎥 Old Camera: Recording OFF")

# Adapter
class SecurityCameraSystem(Observer):
    """Adapter: Wraps OldCameraSystem to match SmartCity interface."""
    def __init__(self):
        self.camera = OldCameraSystem()

    def activate(self):
        self.camera.enable_recording()
    def deactivate(self):
        self.camera.disable_recording()

    # Observer implementation
    def update(self, event: str, data=None):
        if event == "intrusion":
            print('🚨 Security Alert: Intrusion detected!')  # ← THIS LINE IS REQUIRED
            self.activate()