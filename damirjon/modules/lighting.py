# lighting.py
# PATTERN: Adapter – tashqi yorug‘lik API bilan ishlaydi.

from core.adapter import ExternalLightingAPI, LightingAdapter

class LightingSystem:
    """Lighting subsystem"""

    def __init__(self):
        self.adapter = LightingAdapter(ExternalLightingAPI())

    def turn_on_lights(self):
        print("[Lighting] Turning on city lights...")
        self.adapter.turn_on()
