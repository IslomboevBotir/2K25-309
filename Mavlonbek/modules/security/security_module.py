# FIO/modules/security/security_module.py

from FIO.core.adapters.adapter import LegacySecurityCamera, SecurityCameraAdapter, ModernSecurityDevice

# --- Decorator Implementation ---

class SecurityFeedDecorator(ModernSecurityDevice):
    """
    Design Pattern: Decorator (Structural)
    Purpose: Attaches additional responsibilities to an object dynamically.
    Usage: Adds logging and encryption features to the base security feed object.
    """
    def __init__(self, device: ModernSecurityDevice):
        self._device = device

    def start_feed(self):
        # Pre-operation: Add encryption
        print("Decorator: Encrypting security feed...")
        result = self._device.start_feed()
        # Post-operation: Add logging
        print("Decorator: Logging feed activity...")
        return f"Encrypted and Logged: {result}"

# --- Security Module ---

class SecurityModule:
    """
    Integrates the Adapter and Decorator patterns.
    """
    def __init__(self):
        # 1. Adapter Usage: Integrate the legacy camera
        legacy_camera = LegacySecurityCamera()
        adapted_camera = SecurityCameraAdapter(legacy_camera)
        
        # 2. Decorator Usage: Decorate the adapted camera with extra features
        self.security_feed = SecurityFeedDecorator(adapted_camera)
        print("Security Module: Initialized with an adapted and decorated camera feed.")

    def deploy_security_system(self):
        print("Security Module: City-wide security system deployed.")

    def check_feed(self):
        print(self.security_feed.start_feed())

    def get_status(self):
        print("Security Module Status: Security feed is active and monitored.")
