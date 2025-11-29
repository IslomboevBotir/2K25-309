class StreetLight:
    def __init__(self):
        self.location = "Ko'cha"
        self.brightness = 60
        self.auto_mode = True
        self.sensor = False

    def __str__(self):
        return f"{self.location} | {self.brightness}% | Auto: {self.auto_mode} | Sensor: {self.sensor}"

class StreetLightBuilder:
    def __init__(self):
        self.light = StreetLight()

    def set_location(self, loc): self.light.location = loc; return self
    def set_brightness(self, b): self.light.brightness = max(0, min(100, b)); return self
    def set_auto_mode(self, mode): self.light.auto_mode = mode; return self
    def with_sensor(self): self.light.sensor = True; return self

    def build(self):
        print(f"[Builder] Chiroq tayyor: {self.light.location}")
        return self.light