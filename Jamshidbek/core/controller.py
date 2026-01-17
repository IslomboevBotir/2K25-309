from Jamshidbek.core.config import CityConfig
from Jamshidbek.core.factories.subsystem_factory import DefaultCityFactory


class SmartCityController:
    """
    Singleton + Facade Pattern:
    - Singleton: only one controller instance exists.
    - Facade: unified interface to manage all subsystems.
    """
    _instance = None

    def __new__(cls, config: CityConfig):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, config: CityConfig):
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        self.config = config
        self.factory = DefaultCityFactory(
            city_name=config.city_name,
            eco_mode=config.eco_mode,
            role=config.default_role,
        )

        self.lighting = self.factory.create_lighting()
        self.transport = self.factory.create_transport()
        self.security = self.factory.create_security()
        self.energy = self.factory.create_energy()
        self.weather = self.factory.create_weather()

    # Facade methods
    def set_role(self, role: str) -> str:
        self.security.set_role(role)
        return f"Role set to: {role}"

    def city_status(self) -> str:
        lines = [f"=== {self.config.city_name} STATUS ==="]
        lines.append(self.weather.get_summary())
        lines.append(self.lighting.status())
        lines.append(self.transport.status())
        lines.append(self.security.status())
        lines.append(self.energy.status())
        return "\n".join(lines)

    # Lighting
    def lighting_on(self) -> str:
        return self.lighting.turn_on()

    def lighting_off(self) -> str:
        return self.lighting.turn_off()

    def lighting_brightness(self, value: int) -> str:
        return self.lighting.set_brightness(value)

    # Transport
    def transport_set_traffic(self, level: int) -> str:
        return self.transport.set_traffic_level(level)

    def transport_optimize(self) -> str:
        return self.transport.optimize_routes()

    def transport_toggle_signals(self) -> str:
        return self.transport.toggle_signals_mode()

    # Security
    def security_arm(self) -> str:
        return self.security.arm()

    def security_disarm(self) -> str:
        return self.security.disarm()

    def security_add_alert(self, msg: str) -> str:
        return self.security.add_alert(msg)

    def security_alerts(self) -> str:
        return self.security.recent_alerts()

    # Energy
    def energy_toggle(self) -> str:
        return self.energy.toggle_saving_mode()
