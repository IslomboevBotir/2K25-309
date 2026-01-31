"""
Security subsystem devices
"""


class SecurityCamera:
    """Security camera device"""
    
    def __init__(self, device_id: str, location: str):
        self.device_id = device_id
        self.location = location
        self.is_recording = False
        self.resolution = "1080p"
    
    def start(self):
        """Start recording"""
        self.is_recording = True
        print(f"[CAMERA] {self.device_id} at {self.location}: RECORDING START")
    
    def stop(self):
        """Stop recording"""
        self.is_recording = False
        print(f"[CAMERA] {self.device_id} at {self.location}: RECORDING STOP")
    
    def status(self) -> dict:
        """Get camera status"""
        return {
            'device_id': self.device_id,
            'location': self.location,
            'is_recording': self.is_recording,
            'resolution': self.resolution
        }
