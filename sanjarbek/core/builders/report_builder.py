# core/builders/report_builder.py

class CityReportBuilder:
    """
    Pattern: Builder (Yaratish)

    Maqsad:
    Murakkab matnli hisobotni bosqichma-bosqich qurish, boshqaruvchi kodini toza saqlash.

    Nima uchun Builder?
    - Hisobot tuzilmasi oson kengayadi (ko‘proq bo‘limlar, formatlash, vaqtlar va boshqalar)
    - Boshqaruvchi (controller) faqat qismlarni yig‘ishni so‘raydi, tafsilotlarni builder bajaradi.
    """

    def __init__(self):
        self._lines: list[str] = []

    def add_header(self, title: str) -> "CityReportBuilder":
        self._lines.append("=" * 50)
        self._lines.append(title)
        self._lines.append("=" * 50)
        return self

    def add_section(self, name: str, content: str) -> "CityReportBuilder":
        self._lines.append(f"\n[{name}]")
        self._lines.append(content)
        return self

    def add_footer(self, text: str) -> "CityReportBuilder":
        self._lines.append("\n" + "-" * 50)
        self._lines.append(text)
        return self

    def build(self) -> str:
        return "\n".join(self._lines)
