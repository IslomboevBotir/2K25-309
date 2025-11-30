# FIO/core/adapters/adapter.py

# --- Adaptee (The existing, incompatible class) ---

class LegacySecurityCamera:
    """
    The existing class with an incompatible interface.
    It uses a proprietary method name.
    """
    def start_proprietary_feed(self):
        return "Legacy camera feed started: Transmitting video data via proprietary protocol."

# --- Target Interface (The interface the client expects) ---

class ModernSecurityDevice:
    """The interface that the SecurityModule expects all devices to implement."""
    def start_feed(self):
        raise NotImplementedError

# --- Adapter ---

class SecurityCameraAdapter(ModernSecurityDevice):
    """
    Design Pattern: Adapter (Structural)
    Purpose: Converts the interface of a class (LegacySecurityCamera) into another interface
             (ModernSecurityDevice) that clients expect.
    Usage: Allows the SecurityModule to seamlessly integrate the legacy camera.
    """
    def __init__(self, legacy_camera: LegacySecurityCamera):
        self._legacy_camera = legacy_camera

    def start_feed(self):
        # The adapter translates the call to the Adaptee's specific method
        print("Adapter: Translating request to legacy camera protocol...")
        return self._legacy_camera.start_proprietary_feed()
