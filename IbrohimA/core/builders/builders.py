"""
Builder Naqshi Implementatsiyasi
Foydalanish: SmartCity konfiguratsiyasini bosqichma-bosqich yaratish
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class SmartCityKonfiguratsiya:
    """SmartCity Tizimi uchun Konfiguratsiya"""
    shahar_nomi: str = "AqliShahar"
    yoritish_qurilmalari: int = 0
    xavfsizlik_kameralari: int = 0
    harakat_chiroqlari: int = 0
    energiya_monitorlari: int = 0
    avtomatik_ishga_tushirish: bool = False
    jurnallash_yoqilgan: bool = True
    qurilma_konfigurasiyalari: Dict[str, dict] = field(default_factory=dict)
    
    # English property aliases for backward compatibility
    @property
    def city_name(self) -> str:
        return self.shahar_nomi
    
    @property
    def num_lighting_devices(self) -> int:
        return self.yoritish_qurilmalari
    
    @property
    def num_security_cameras(self) -> int:
        return self.xavfsizlik_kameralari
    
    @property
    def num_traffic_lights(self) -> int:
        return self.harakat_chiroqlari
    
    @property
    def num_energy_monitors(self) -> int:
        return self.energiya_monitorlari
    
    @property
    def auto_start(self) -> bool:
        return self.avtomatik_ishga_tushirish
    
    @property
    def logging_enabled(self) -> bool:
        return self.jurnallash_yoqilgan
    
    @property
    def log_enabled(self) -> bool:
        """Alias for logging_enabled for backward compatibility"""
        return self.jurnallash_yoqilgan
    
    @property
    def device_configs(self) -> Dict[str, dict]:
        return self.qurilma_konfigurasiyalari


class SmartCityBiluvchi:
    """
    Builder Naqshi - SmartCity konfiguratsiyasini bosqichma-bosqich yaratadi.
    Ko'p sonli konstruktorlar yaratmasdan turli konfiguratsiyalarni yaratish imkonini beradi.
    """
    
    def __init__(self, shahar_nomi: str = "AqliShahar"):
        self.config = SmartCityKonfiguratsiya(shahar_nomi=shahar_nomi)
    
    def add_lighting_system(self, num_devices: int, locations: List[str] = None) -> 'SmartCityBiluvchi':
        """Yoritish subsistemasi qo'shish"""
        self.config.yoritish_qurilmalari = num_devices
        if locations is None:
            locations = [f"Hudud-{i+1}" for i in range(num_devices)]
        self.config.qurilma_konfigurasiyalari['lighting'] = {'locations': locations}
        return self
    
    def add_security_system(self, num_cameras: int, locations: List[str] = None) -> 'SmartCityBiluvchi':
        """Xavfsizlik subsistemasi qo'shish"""
        self.config.xavfsizlik_kameralari = num_cameras
        if locations is None:
            locations = [f"Zone-{i+1}" for i in range(num_cameras)]
        self.config.qurilma_konfigurasiyalari['security'] = {'locations': locations}
        return self
    
    def add_transport_system(self, num_lights: int, intersections: List[str] = None) -> 'SmartCityBiluvchi':
        """Transport subsistemasi qo'shish"""
        self.config.harakat_chiroqlari = num_lights
        if intersections is None:
            intersections = [f"Chorrahadni-{i+1}" for i in range(num_lights)]
        self.config.qurilma_konfigurasiyalari['transport'] = {'intersections': intersections}
        return self
    
    def add_energy_system(self, num_monitors: int, zones: List[str] = None) -> 'SmartCityBiluvchi':
        """Energiya subsistemasi qo'shish"""
        self.config.energiya_monitorlari = num_monitors
        if zones is None:
            zones = [f"Zone-{i+1}" for i in range(num_monitors)]
        self.config.qurilma_konfigurasiyalari['energy'] = {'zones': zones}
        return self
    
    def set_auto_start(self, auto_start: bool = True) -> 'SmartCityBiluvchi':
        """Initsializatsiyada avtomatik ishga tushirish yoq/yoq"""
        self.config.avtomatik_ishga_tushirish = auto_start
        return self
    
    def enable_logging(self, enabled: bool = True) -> 'SmartCityBiluvchi':
        """Jurnallashni yoq/o'chir"""
        self.config.jurnallash_yoqilgan = enabled
        return self
    
    def build(self) -> SmartCityKonfiguratsiya:
        """Konfiguratsiyani yaratish va qaytarish"""
        return self.config


# Eski kod uchun
SmartCityConfig = SmartCityKonfiguratsiya
SmartCityBuilder = SmartCityBiluvchi
