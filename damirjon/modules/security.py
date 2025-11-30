# security.py
# PATTERN: Proxy – xavfsizlik tekshiruvini boshqaradi (kirishni cheklash).

class SecurityCamera:
    """Real camera object"""

    def scan(self):
        print("[Camera] Area scanned. All safe.")

class SecurityProxy:
    """Proxy – kamera ishini nazorat qilib, ruxsat bilan ishlatadi."""

    def __init__(self):
        self.camera = SecurityCamera()
        self.authorized = False

    def authenticate(self, key: str):
        if key == "admin123":
            self.authorized = True
            print("[Proxy] Access granted.")
        else:
            print("[Proxy] Access denied.")

    def scan(self):
        if not self.authorized:
            print("[Proxy] Unauthorized access! Cannot scan.")
        else:
            self.camera.scan()

class SecuritySystem:
    def __init__(self):
        self.proxy = SecurityProxy()
        self.proxy.authenticate("admin123")   # Auto-auth for demo

    def scan_area(self):
        self.proxy.scan()
