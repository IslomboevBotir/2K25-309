class Light:
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def status(self):
        pass

class BasicLight(Light):
    def __init__(self, light_id: int):
        self.id = light_id
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"💡 Light {self.id} → ON")

    def turn_off(self):
        self.is_on = False
        print(f"💡 Light {self.id} → OFF")

    def status(self):
        state = "ON ✅" if self.is_on else "OFF ❌"
        print(f"💡 Light {self.id} status: {state}")

class LightGroup(Light):
    def __init__(self, group_name: str):
        self.name = group_name
        self.children: list[Light] = []

    def add(self, light: Light):
        self.children.append(light)

    def turn_on(self):
        print(f"\n🌟 Group '{self.name}' → activating all lights")
        for light in self.children:
            light.turn_on()

    def turn_off(self):
        print(f"\n🌙 Group '{self.name}' → disabling all lights")
        for light in self.children:
            light.turn_off()

    def status(self):
        print(f"\n💡 Checking status for group: {self.name}")
        for child in self.children:
            child.status()

class LoggingDecorator(Light):
    def __init__(self, wrapped: Light):
        self.wrapped = wrapped

    def turn_on(self):
        print(f"[LOG] Turning on light...")
        self.wrapped.turn_on()

    def turn_off(self):
        print(f"[LOG] Turning off light...")
        self.wrapped.turn_off()

    def status(self):
        self.wrapped.status()

class LightingModule:
    def __init__(self):
        self.root_group = LightGroup("City Main Lights")
        for i in range(1, 6):
            self.root_group.add(LoggingDecorator(BasicLight(i)))

    def start(self):
        print("💡 Lighting module started")

    def status(self):
        print(self.root_group.status())
