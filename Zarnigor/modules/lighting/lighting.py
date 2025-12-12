"""
Lighting subsystem implementing:
- Composite Pattern (Light, BasicLight, LightGroup)
- Decorator Pattern (LoggingDecorator)
- LightingSystem as a facade over the internal lighting structure.
"""


class Light:
    """
    Component interface for the Composite pattern.
    Both individual lights and groups implement this interface.
    """

    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError


class BasicLight(Light):
    """
    Leaf element in the Composite structure.
    Represents a single street light.
    """

    def __init__(self, light_id: int):
        self.id = light_id
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"💡 Light {self.id} → ON")

    def turn_off(self):
        self.is_on = False
        print(f"💡 Light {self.id} → OFF")

    def status(self) -> bool:
        state = "ON ✅" if self.is_on else "OFF ❌"
        print(f"💡 Light {self.id} status: {state}")
        return self.is_on


class LightGroup(Light):
    """
    Composite element that can contain multiple Light objects
    (both BasicLight and other LightGroup instances).
    """

    def __init__(self, group_name: str):
        self.name = group_name
        self.children: list[Light] = []

    def add(self, light: Light):
        self.children.append(light)

    def remove(self, light: Light):
        if light in self.children:
            self.children.remove(light)

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
    """
    Decorator for Light objects.

    Adds simple logging messages around core operations (turn_on, turn_off)
    without modifying the underlying Light implementation.
    """

    def __init__(self, wrapped: Light):
        self.wrapped = wrapped

    def turn_on(self):
        print("[LOG] Turning on light...")
        self.wrapped.turn_on()

    def turn_off(self):
        print("[LOG] Turning off light...")
        self.wrapped.turn_off()

    def status(self):
        return self.wrapped.status()


class LightingSystem:
    """
    Facade for the lighting subsystem.

    Internally uses a Composite tree of lights and Decorators for logging,
    but exposes simple methods for the rest of the system.
    """

    def __init__(self):
        # Root group representing all city lights
        self.root_group = LightGroup("City Main Lights")

        # Simple example: 5 basic lights, each wrapped with logging decorator
        for i in range(1, 6):
            self.root_group.add(LoggingDecorator(BasicLight(i)))

    def get_status(self) -> str:
        """
        Displays status for all lights and returns a summary string.
        """
        print("\n📊 Lighting System Status:")
        self.root_group.status()
        return "Lighting system operational."

    def turn_all_on(self):
        self.root_group.turn_on()

    def turn_all_off(self):
        self.root_group.turn_off()
