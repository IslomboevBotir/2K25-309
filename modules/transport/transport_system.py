"""
Transportation System Components
"""

from core.factories.device_factory import SmartDevice


class TrafficLight(SmartDevice):
    """Smart traffic light device"""
    
    def __init__(self, device_id: str, location: str):
        super().__init__(device_id, location)
        self.current_state = "red"
    
    def activate(self):
        self.is_active = True
        print(f"🚦 Traffic light {self.device_id} activated at {self.location}")
    
    def deactivate(self):
        self.is_active = False
        self.current_state = "red"
        print(f"🚦 Traffic light {self.device_id} deactivated")
    
    def set_state(self, state: str):
        """Set traffic light state"""
        if state in ["red", "yellow", "green"]:
            self.current_state = state
            symbol = "🔴" if state == "red" else "🟡" if state == "yellow" else "🟢"
            print(f"  {symbol} {self.location}: {state.upper()}")
        else:
            print(f"  ❌ Invalid state: {state}")
    
    def get_status(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        return f"{self.location}: {self.current_state.upper()} ({status})"


class PublicTransport(SmartDevice):
    """Public transport vehicle"""
    
    def __init__(self, device_id: str, location: str):
        super().__init__(device_id, location)
        self.route = location
        self.is_running = False
    
    def activate(self):
        self.is_active = True
        self.is_running = True
        print(f"🚌 Public transport {self.device_id} started on {self.route}")
    
    def deactivate(self):
        self.is_active = False
        self.is_running = False
        print(f"🚌 Public transport {self.device_id} stopped")
    
    def start_route(self):
        """Start the transport route"""
        if self.is_active:
            self.is_running = True
            print(f"  ✓ Route {self.route} is now running")
        else:
            print(f"  ❌ Cannot start inactive transport")
    
    def stop_route(self):
        """Stop the transport route"""
        self.is_running = False
        print(f"  ✓ Route {self.route} stopped")
    
    def get_status(self) -> str:
        status = "Running" if self.is_running else "Stopped"
        return f"{self.route}: {status}"