"""
Builder module.

Implements the Builder design pattern to construct a complex, multi-section
city report step by step, separating the construction logic (Director)
from the representation (Builder).
"""


class CityReportBuilder:
    """
    Concrete Builder responsible for assembling different parts
    of a city report. The result is a simple string, but the process
    is decomposed into multiple steps.
    """

    def __init__(self):
        self._parts: list[str] = []

    def add_header(self, title: str):
        self._parts.append(f"=== {title} ===")

    def add_section(self, name: str, content: str):
        self._parts.append(f"[{name}] {content}")

    def add_footer(self, text: str):
        self._parts.append(f"--- {text} ---")

    def reset(self):
        self._parts.clear()

    def get_result(self) -> str:
        """
        Returns the final report string.
        """
        return "\n".join(self._parts)


class CityReportDirector:
    """
    Director that defines the building steps and their order.
    """

    def __init__(self, builder: CityReportBuilder):
        self.builder = builder

    def build_full_report(
        self,
        transport_status: str,
        lighting_status: str,
        security_status: str,
        energy_status: str,
    ):
        self.builder.add_header("SmartCity Daily Report")
        self.builder.add_section("Transport status", transport_status)
        self.builder.add_section("Lighting status", lighting_status)
        self.builder.add_section("Security status", security_status)
        self.builder.add_section("Energy status", energy_status)
        self.builder.add_footer("End of report")
