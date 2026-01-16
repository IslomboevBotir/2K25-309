"""
Security System with Proxy Pattern

Design Pattern: PROXY
Purpose: Controls access to security devices with authentication
"""

from abc import ABC, abstractmethod
from datetime import datetime


class SecurityDevice(ABC):
    """Abstract security device interface"""
    
    @abstractmethod
    def activate(self):
        pass
    
    @abstractmethod
    def monitor(self):
        pass
    
    @abstractmethod
    def get_status(self) -> str:
        pass


class Camera(SecurityDevice):
    """Real security camera"""
    
    def __init__(self, location: str):
        self.location = location
        self.is_recording = False
        self.footage_count = 0
    
    def activate(self):
        self.is_recording = True
        print(f"📹 Camera at {self.location} activated")
    
    def monitor(self):
        if self.is_recording:
            self.footage_count += 1
            print(f"  👁️  Monitoring {self.location} (footage: {self.footage_count})")
        else:
            print(f"  ❌ Camera not activated")
    
    def get_status(self) -> str:
        status = "Recording" if self.is_recording else "Standby"
        return f"{self.location}: {status} (footage: {self.footage_count})"


class AlarmSystem(SecurityDevice):
    """Real alarm system"""
    
    def __init__(self, location: str):
        self.location = location
        self.is_armed = False
        self.alert_count = 0
    
    def activate(self):
        self.is_armed = True
        print(f"🚨 Alarm at {self.location} armed")
    
    def monitor(self):
        if self.is_armed:
            print(f"  ⚠️  Monitoring {self.location} for intrusions")
        else:
            print(f"  ❌ Alarm not armed")
    
    def trigger_alert(self):
        if self.is_armed:
            self.alert_count += 1
            print(f"  🔔 ALERT! Intrusion detected at {self.location}")
    
    def get_status(self) -> str:
        status = "Armed" if self.is_armed else "Disarmed"
        return f"{self.location}: {status} (alerts: {self.alert_count})"


class SecurityDeviceProxy(SecurityDevice):
    """
    Proxy Pattern
    Controls access to security devices with authentication
    """
    
    def __init__(self, real_device: SecurityDevice, access_level: str = "guest"):
        self._real_device = real_device
        self._access_level = access_level
        self._access_log = []
    
    def _check_access(self, required_level: str) -> bool:
        """Check if user has required access level"""
        levels = {"guest": 0, "user": 1, "admin": 2}
        user_level = levels.get(self._access_level, 0)
        req_level = levels.get(required_level, 0)
        return user_level >= req_level
    
    def _log_access(self, action: str, granted: bool):
        """Log access attempt"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        status = "✓ GRANTED" if granted else "✗ DENIED"
        self._access_log.append(f"[{timestamp}] {action}: {status}")
    
    def activate(self):
        """Requires admin access"""
        if self._check_access("admin"):
            print(f"🔓 Access granted ({self._access_level})")
            self._log_access("ACTIVATE", True)
            self._real_device.activate()
        else:
            print(f"🔒 Access denied - Admin rights required")
            self._log_access("ACTIVATE", False)
    
    def monitor(self):
        """Requires user access"""
        if self._check_access("user"):
            self._log_access("MONITOR", True)
            self._real_device.monitor()
        else:
            print(f"🔒 Access denied - User rights required")
            self._log_access("MONITOR", False)
    
    def get_status(self) -> str:
        """Anyone can view status"""
        return self._real_device.get_status()
    
    def get_access_log(self) -> list:
        """Get access log (admin only)"""
        if self._check_access("admin"):
            return self._access_log
        return ["Access denied"]