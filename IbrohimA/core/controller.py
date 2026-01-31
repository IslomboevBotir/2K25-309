"""
Asosiy Kontroler - Singleton va Facade naqshlarini birlashtiradi
"""

from core.singelton.singleton import Singleton
from core.proxy.proxy import SubsistemProxy, SubsystemProxy
from core.adapters.adapters import MonitoringDekorator, SecurityDekorator, LoggingDekorator
from core.adapters.adapters import MonitoringDecorator, SecurityDecorator, LoggingDecorator
from core.factories.factories import (
    YoritishQurilmaFabriki as LightingDeviceFactory,
    XavfsizlikQurilmaFabriki as SecurityDeviceFactory,
    TransportQurilmaFabriki as TransportDeviceFactory,
    EnergiyaQurilmaFabriki as EnergyDeviceFactory
)
from modules.lighting.lighting_system import LightingSystem
from modules.security import SecuritySystem
from modules.transport import TransportSystem
from modules.energy import EnergySystem
from typing import Dict, Any


class SmartCityController(Singleton):
    """
    SmartCity Kontroleri - Markaziy boshqaruv tizimi
    
    Qo'llaniladigan Dizayn Naqshlari:
    - Singleton: Faqat bitta kontroler instansiyasini ta'minlaydi
    - Facade: Barcha subsistemalar uchun yagona interfeys taqdim etadi
    - Proxy: Subsistemalar kirish huquqini boshqaradi
    - Decorator: Monitoring/xavfsizlik/jurnallash qo'shimchasini qo'shadi
    """
    
    def __init__(self):
        super().__init__()
        if not hasattr(self, '_initialized'):
            self._initialized = False
            self._subsystems: Dict[str, Any] = {}
            self._factories = {}
            self._is_running = False
    
    def initialize(self):
        """SmartCity Kontrolerini initsializatsiya qilish"""
        if self._initialized:
            print("[KONTROLER] Allaqachon initsializatsiya qilingan")
            return
        
        print("\n" + "="*60)
        print("🏙️  SMARTCITY KONTROLERI INITSIALIZATSIYA QILINYAPTI")
        print("="*60)
        
        # Subsistemalarni initsializatsiya qilish
        lighting_system = LightingSystem()
        security_system = SecuritySystem()
        transport_system = TransportSystem()
        energy_system = EnergySystem()
        
        # Subsistemalarni Proxy bilan o'ra berish kirish nazorati uchun
        self._subsystems = {
            'lighting': SubsystemProxy(lighting_system),
            'security': SubsystemProxy(security_system),
            'transport': SubsystemProxy(transport_system),
            'energy': SubsystemProxy(energy_system)
        }
        
        # Kengaytirilgan funksionallik uchun dekoratorlarni qo'shish
        self._subsystems['lighting'] = MonitoringDecorator(
            self._subsystems['lighting']
        )
        self._subsystems['security'] = SecurityDecorator(
            self._subsystems['security'],
            auth_level="admin"
        )
        self._subsystems['energy'] = LoggingDecorator(
            self._subsystems['energy']
        )
        
        # Fabrikalarni initsializatsiya qilish
        self._factories = {
            'lighting': LightingDeviceFactory(),
            'security': SecurityDeviceFactory(),
            'transport': TransportDeviceFactory(),
            'energy': EnergyDeviceFactory()
        }
        
        # Barcha subsistemalarni initsializatsiya qilish
        for subsystem_name, subsystem in self._subsystems.items():
            if hasattr(subsystem, 'initialize'):
                subsystem.initialize()
        
        self._initialized = True
        self._is_running = True
        print("[KONTROLER] ✓ SmartCity Kontroleri muvaffaqiyatli initsializatsiya qilindi\n")
    
    def create_device(self, subsystem_type: str, device_id: str, location: str):
        """
        Tegishli fabric dan foydalanib qurilma yaratish
        Factory Naqshining namunasi
        """
        if subsystem_type not in self._factories:
            print(f"[KONTROLER] XATO: Noma'lum subsistema turi: {subsystem_type}")
            return None
        
        factory = self._factories[subsystem_type]
        device = factory.create_device(device_id, location)
        print(f"[KONTROLER] Qurilma yaratildi: {device_id} - {factory.get_factory_name()}")
        return device
    
    def add_device_to_subsystem(self, subsystem_name: str, device_id: str, device):
        """Subsistemaga qurilma qo'shish"""
        if subsystem_name not in self._subsystems:
            print(f"[KONTROLER] XATO: Noma'lum subsistema: {subsystem_name}")
            return False
        
        # Haqiqiy subsistemani olish (dekoratorlardan chiqarish)
        subsystem = self._subsystems[subsystem_name]
        while hasattr(subsystem, '_subsystem'):
            subsystem = subsystem._subsystem
        while hasattr(subsystem, '_real_subsystem'):
            subsystem = subsystem._real_subsystem
        
        if hasattr(subsystem, 'add_device'):
            subsystem.add_device(device_id, device)
            return True
        return False
    
    def get_subsystem_status(self, subsystem_name: str) -> Dict[str, Any]:
        """Muayyan subsistemaning statusini olish"""
        if subsystem_name not in self._subsystems:
            print(f"[KONTROLER] XATO: Noma'lum subsistema: {subsystem_name}")
            return {}
        
        subsystem = self._subsystems[subsystem_name]
        if hasattr(subsystem, 'get_status'):
            return subsystem.get_status()
        return {}
    
    def get_all_status(self) -> Dict[str, Dict[str, Any]]:
        """Barcha subsistemalarning statusini olish"""
        status = {
            'kontroler_ishlamoqda': self._is_running,
            'subsistemalar': {}
        }
        
        for name in self._subsystems:
            status['subsistemalar'][name] = self.get_subsystem_status(name)
        
        return status
    
    def start_subsystem(self, subsystem_name: str):
        """Muayyan subsistemani ishga tushirish"""
        if subsystem_name not in self._subsystems:
            print(f"[KONTROLER] XATO: Noma'lum subsistema: {subsystem_name}")
            return
        
        subsystem = self._subsystems[subsystem_name]
        # Haqiqiy subsistemani start_all chaqirish uchun olish
        real_sys = subsystem
        while hasattr(real_sys, '_subsystem'):
            real_sys = real_sys._subsystem
        while hasattr(real_sys, '_real_subsystem'):
            real_sys = real_sys._real_subsystem
        
        if hasattr(real_sys, 'start_all'):
            real_sys.start_all()
    
    def stop_subsystem(self, subsystem_name: str):
        """Muayyan subsistemani to'xtatish"""
        if subsystem_name not in self._subsystems:
            print(f"[KONTROLER] XATO: Noma'lum subsistema: {subsystem_name}")
            return
        
        subsystem = self._subsystems[subsystem_name]
        # Haqiqiy subsistemani stop_all chaqirish uchun olish
        real_sys = subsystem
        while hasattr(real_sys, '_subsystem'):
            real_sys = real_sys._subsystem
        while hasattr(real_sys, '_real_subsystem'):
            real_sys = real_sys._real_subsystem
        
        if hasattr(real_sys, 'stop_all'):
            real_sys.stop_all()
    
    def start_all_subsystems(self):
        """Barcha subsistemalarni ishga tushirish"""
        print("\n[KONTROLER] Barcha subsistemalar ishga tushurilmoqda...")
        for subsystem_name in self._subsystems:
            self.start_subsystem(subsystem_name)
        print("[KONTROLER] ✓ Barcha subsistemalar ishga tushurildi\n")
    
    def stop_all_subsystems(self):
        """Barcha subsistemalarni to'xtatish"""
        print("\n[KONTROLER] Barcha subsistemalar to'xtatilmoqda...")
        for subsystem_name in self._subsystems:
            self.stop_subsystem(subsystem_name)
        print("[KONTROLER] ✓ Barcha subsistemalar to'xtatildi\n")
    
    def shutdown(self):
        """Kontroler va barcha subsistemalarni o'chirish"""
        print("\n" + "="*60)
        print("🔴 SMARTCITY KONTROLERI O'CHIRILMOQDA")
        print("="*60)
        
        self.stop_all_subsystems()
        
        for subsystem in self._subsystems.values():
            if hasattr(subsystem, 'shutdown'):
                subsystem.shutdown()
        
        self._is_running = False
        print("[KONTROLER] ✓ SmartCity Kontroleri o'chirildi\n")
    
    def display_menu(self):
        """Asosiy menyuni ko'rsatish"""
        print("\n" + "="*60)
        print("SMARTCITY TIZIMI MENYU")
        print("="*60)
        print("1. Tizim Statusini Ko'rish")
        print("2. Barcha Subsistemalarni Ishga Tushirish")
        print("3. Barcha Subsistemalarni To'xtatish")
        print("4. Qurilma Yaratish va Subsistemaga Qo'shish")
        print("5. Muayyan Subsistemani Ishga Tushirish")
        print("6. Muayyan Subsistemani To'xtatish")
        print("7. Tizim Ma'lumotlari")
        print("0. Chiqish")
        print("="*60)
