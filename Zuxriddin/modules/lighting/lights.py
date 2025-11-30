from core.subsystems import LightImplementation

class LEDLight(LightImplementation):
    def turn_on(self):
        print("💡 LED Street Lights: ON")

    def turn_off(self):
        print("💡 LED Street Lights: OFF")

class SolarLight(LightImplementation):
    def turn_on(self):
        print("☀️ Solar-Powered Lights: ON")

    def turn_off(self):
        print("☀️ Solar-Powered Lights: OFF")