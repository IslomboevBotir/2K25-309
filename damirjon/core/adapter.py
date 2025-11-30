# adapter.py
# PATTERN: Adapter – tashqi API/servislar bilan integratsiya qilish.

class ExternalLightingAPI:
    """Tashqi yorug'lik boshqaruv tizimi"""
    def external_turn_on(self):
        print("[External API] Lights powered ON via external service")

class LightingAdapter:
    """Adapter – ExternalLightingAPI uchun moslashtiruvchi qatlam"""

    def __init__(self, external_api: ExternalLightingAPI):
        self.api = external_api

    def turn_on(self):
        self.api.external_turn_on()
