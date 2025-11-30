# FIO/modules/lighting/lighting_module.py

from FIO.core.factories.abstract_factory import BasicDeviceFactory, AdvancedDeviceFactory

class LightingModule:
    """
    Integrates the Abstract Factory pattern to manage different types of lighting devices.
    """
    def __init__(self, factory_type="basic"):
        self.factory = self._get_factory(factory_type)
        self.sensor = self.factory.create_sensor()
        self.actuator = self.factory.create_actuator()
        print(f"Lighting Module: Initialized with {factory_type.capitalize()} devices.")

    def _get_factory(self, factory_type):
        if factory_type.lower() == "basic":
            return BasicDeviceFactory()
        elif factory_type.lower() == "advanced":
            return AdvancedDeviceFactory()
        else:
            raise ValueError("Invalid factory type. Choose 'basic' or 'advanced'.")

    def activate_smart_lighting(self):
        print("Lighting Module: Smart lighting system activated.")
        print(f"Sensor Action: {self.sensor.monitor()}")
        print(f"Actuator Action: {self.actuator.actuate()}")

    def adjust_brightness_for_saving(self):
        print("Lighting Module: Adjusting brightness for energy saving.")
        # This is where the actuator would be commanded to a lower setting
        print(f"Actuator Action: {self.actuator.actuate()} (Energy Saving Mode)")

    def get_status(self):
        print(f"Lighting Module Status: Active with {self.factory.__class__.__name__} devices.")
