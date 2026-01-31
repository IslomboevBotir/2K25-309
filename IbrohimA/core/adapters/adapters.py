"""
Decorator Naqshi Implementatsiyasi
Foydalanish: Subsistemalar funksionalligini dinamik qo'shish
"""

from abc import ABC, abstractmethod


class ISubsistemDekorator(ABC):
    """Subsistema dekoratorlari uchun interfeys"""
    
    @abstractmethod
    def get_status(self) -> dict:
        pass


class SubsistemDekorator(ISubsistemDekorator):
    """
    Decorator Naqshi - Ob'ektga dinamik qo'shimcha javobgarliklar qo'shadi.
    Funksionalligini kengaytirish uchun merosga bo'g'lanmay moslashuvchan alternativa taqdim etadi.
    """
    
    def __init__(self, subsystem):
        self._subsystem = subsystem
    
    def get_status(self) -> dict:
        """O'rab olingan subsistemadan statusni olish"""
        return self._subsystem.get_status()


class MonitoringDekorator(SubsistemDekorator):
    """Subsistemalar uchun monitoring qobiliyatlari qo'shadi
    (Monitoring xususiyatlarini dinamik qo'shadi)
    """
    
    def __init__(self, subsystem):
        super().__init__(subsystem)
        self._monitoring_enabled = True
        self._event_count = 0
    
    def get_status(self) -> dict:
        """Statusga monitoring metrikalarini qo'shish"""
        status = self._subsystem.get_status()
        status['monitoring_enabled'] = self._monitoring_enabled
        status['event_count'] = self._event_count
        return status
    
    def record_event(self, event: str):
        """Kuzatiladigan voqea qayd qilish"""
        self._event_count += 1
        print(f"[MONITORING] Voqea qayd qilindi: {event} (Jami: {self._event_count})")


# Create English alias
MonitoringDecorator = MonitoringDekorator


class SecurityDekorator(SubsistemDekorator):
    """Subsistemalar uchun xavfsizlik xususiyatlarini qo'shadi"""
    
    def __init__(self, subsystem, auth_level: str = "user"):
        super().__init__(subsystem)
        self._auth_level = auth_level
        self._is_locked = False
    
    def get_status(self) -> dict:
        """Statusga xavfsizlik ma'lumotlarini qo'shish"""
        status = self._subsystem.get_status()
        status['security_auth_level'] = self._auth_level
        status['is_locked'] = self._is_locked
        return status
    
    def lock(self):
        """Subsistemani qulf qilish"""
        self._is_locked = True
        print(f"[SECURITY] Subsistema qulfland (Ruxsat darajasi: {self._auth_level})")
    
    def unlock(self, password: str = None) -> bool:
        """Subsistemani qulfdan chiqarish"""
        if self._auth_level == "admin" and password == "admin123":
            self._is_locked = False
            print("[SECURITY] Subsistema qulfdan chiqarildi")
            return True
        elif self._auth_level == "user":
            self._is_locked = False
            print("[SECURITY] Subsistema qulfdan chiqarildi")
            return True
        return False


class LoggingDekorator(SubsistemDekorator):
    """Subsistemalar uchun jurnallash qobiliyatlari qo'shadi"""
    
    def __init__(self, subsystem):
        super().__init__(subsystem)
        self._logs = []
    
    def get_status(self) -> dict:
        """Statusga jurnallash ma'lumotlarini qo'shish"""
        status = self._subsystem.get_status()
        status['log_count'] = len(self._logs)
        status['logs'] = self._logs[-5:] if self._logs else []  # Oxirgi 5 ta jurnal
        return status
    
    def add_log(self, message: str):
        """Jurnal yozuvini qo'shish"""
        self._logs.append(message)
        print(f"[LOGGING] {message}")


# Eski kod uchun - English aliases
# The Uzbek and English names are the same, so no renaming needed
# MonitoringDekorator, SecurityDekorator, LoggingDekorator work as both Uzbek and English
ISubsystemDecorator = ISubsistemDekorator
SubsystemDecorator = SubsistemDekorator

# Decorator aliases - English versions of Uzbek classes
MonitoringDecorator = MonitoringDekorator
SecurityDecorator = SecurityDekorator
LoggingDecorator = LoggingDekorator
