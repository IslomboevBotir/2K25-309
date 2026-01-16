# core/controller.py

from core.adapters.weather_adapter import WeatherServiceAdapter
from core.builders.report_builder import CityReportBuilder
from core.proxy.security_proxy import SecurityProxy

from core.factories.city_factory import CityFactory



# Aqlli shahar boshqaruvchisi
class SmartCityController:
    """
    Dizayn patternlar:
    1) Singleton (Yaratish): Butun tizim uchun faqat bitta boshqaruvchi obyekt bo'lishini ta'minlaydi.
    2) Facade (Struktural): Barcha kichik tizimlarga (transport, yoritish, energiya, xavfsizlik, ob-havo) soddalashtirilgan yagona interfeys beradi.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        # Singleton: faqat bitta obyekt yaratiladi
        if cls._instance is None:
            cls._instance = super(SmartCityController, cls).__new__(cls)
        return cls._instance

    def __init__(self, factory: CityFactory):
        # Singleton uchun qayta initsializatsiyani oldini olamiz
        if getattr(self, "_initialized", False):
            return
        self._initialized = True

        # Kichik tizimlarni Abstract Factory orqali yaratamiz (to'g'ridan-to'g'ri obyekt yaratmaymiz)
        self.transport = factory.create_transport()
        self.lighting = factory.create_lighting()
        self.energy = factory.create_energy()

        real_security = factory.create_security()
        self.security = SecurityProxy(real_security)  # Xavfsizlik tizimi uchun proksi

        # Tashqi xizmatlar uchun adapter
        self.weather = WeatherServiceAdapter()


    # ---------- Facade metodlari (konsol uchun soddalashtirilgan API) ----------

    def show_status(self) -> list[str]:
        """
        Barcha kichik tizimlarning holatini qaytaradi (main.py da chiqarish uchun qulay).
        """
        return [
            self.transport.status(),
            self.lighting.status(),
            self.energy.status(),
            self.security.status(),
        ]

    def transport_dispatch(self, route: str) -> str:
        return self.transport.dispatch(route)

    def lighting_set_brightness(self, level: int) -> str:
        return self.lighting.set_brightness(level)

    def energy_enable_saving_mode(self) -> str:
        return self.energy.enable_saving_mode()

    def energy_disable_saving_mode(self) -> str:
        return self.energy.disable_saving_mode()

    def security_arm(self, token: str) -> str:
        return self.security.arm(token=token)

    def security_disarm(self, token: str) -> str:
        return self.security.disarm(token=token)

    def sync_weather(self) -> str:
        """
        Uses Adapter to get weather info and pushes it to Energy subsystem.
        This creates a logical connection between components.
        """
        info = self.weather.get_current_weather()
        self.energy.update_environment(info)
        return f"Weather synced: {info}"

    def generate_report(self) -> str:
        """
        Pattern: Builder
        Builds a report step-by-step using subsystem statuses.
        """
        builder = CityReportBuilder()
        builder.add_header("SmartCity Daily Report")
        builder.add_section("Transport", self.transport.status())
        builder.add_section("Lighting", self.lighting.status())
        builder.add_section("Energy", self.energy.status())
        builder.add_section("Security", self.security.status())
        builder.add_footer("End of report.")
        return builder.build()
    