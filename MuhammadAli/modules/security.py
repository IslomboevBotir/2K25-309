class Camera:
    def __init__(self, name):
        self.name = name

    def stream(self):
        print(f"   {self.name}: tinch")

class AdvancedSecuritySystem:
    def __init__(self):
        self.cameras = {name: Camera(name) for name in ["Markaziy maydon", "Toshkent stansiyasi", "Alisher Navoiy bog'i"]}
        from smartcity.proxy import SecurityProxy
        self.proxy = SecurityProxy(self)

    def _stream_all(self):
        print("Barcha kameralar jonli efirda:")
        for cam in self.cameras.values():
            cam.stream()

    def get_status(self):
        print("Umumiy xavfsizlik holati: TINCH")
