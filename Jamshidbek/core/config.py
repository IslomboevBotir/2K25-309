from dataclasses import dataclass


@dataclass(frozen=True)
class CityConfig:
    """
    City configuration object.
    Built using Builder pattern (CityConfigBuilder).
    """
    city_name: str
    zones_count: int
    eco_mode: bool
    default_role: str  # "admin" or "guest"
