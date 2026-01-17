from Jamshidbek.core.config import CityConfig


class CityConfigBuilder:
    """
    Builder Pattern:
    Step-by-step construction of CityConfig.
    """
    def __init__(self) -> None:
        self._city_name = "SmartCity"
        self._zones_count = 2
        self._eco_mode = False
        self._default_role = "guest"

    def city_name(self, name: str) -> "CityConfigBuilder":
        self._city_name = (name or "").strip() or "SmartCity"
        return self

    def zones_count(self, n: int) -> "CityConfigBuilder":
        try:
            n = int(n)
        except Exception:
            n = 2
        self._zones_count = max(1, n)
        return self

    def eco_mode(self, enabled: bool) -> "CityConfigBuilder":
        self._eco_mode = bool(enabled)
        return self

    def default_role(self, role: str) -> "CityConfigBuilder":
        role = (role or "").strip().lower()
        self._default_role = role if role in ("admin", "guest") else "guest"
        return self

    def build(self) -> CityConfig:
        return CityConfig(
            city_name=self._city_name,
            zones_count=self._zones_count,
            eco_mode=self._eco_mode,
            default_role=self._default_role,
        )
