"""
Transport subsystem devices
"""


class TrafficLight:
    """Traffic light device"""
    
    def __init__(self, device_id: str, intersection: str):
        self.device_id = device_id
        self.intersection = intersection
        self.current_signal = "red"
        self.is_operational = False
    
    def start(self):
        """Start traffic light operation"""
        self.is_operational = True
        self.current_signal = "red"
        print(f"[TRAFFIC] {self.device_id} at {self.intersection}: OPERATIONAL")
    
    def stop(self):
        """Stop traffic light operation"""
        self.is_operational = False
        self.current_signal = "off"
        print(f"[TRAFFIC] {self.device_id} at {self.intersection}: STOPPED")
    
    def set_signal(self, signal: str):
        """Change traffic signal (red, yellow, green)"""
        if signal in ['red', 'yellow', 'green']:
            self.current_signal = signal
            print(f"[TRAFFIC] {self.device_id}: Signal changed to {signal.upper()}")
    
    def status(self) -> dict:
        """Get traffic light status"""
        return {
            'device_id': self.device_id,
            'intersection': self.intersection,
            'current_signal': self.current_signal,
            'is_operational': self.is_operational
        }
