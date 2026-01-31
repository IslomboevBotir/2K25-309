"""
Proxy Naqshi Implementatsiyasi
Foydalanish: Subsistemamalarga kirish huquqini boshqarish va kechiktirilgan initsializatsiya
"""

from abc import ABC, abstractmethod
from typing import Optional


class ISubsistemProxy(ABC):
    """Subsistema proksylari uchun interfeys"""
    
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def get_status(self) -> dict:
        pass
    
    @abstractmethod
    def execute_command(self, command: str) -> bool:
        pass


class SubsistemProxy(ISubsistemProxy):
    """
    Proxy Naqshi - Boshqa ob'ektning o'rinbosari bo'la xizmat qiladi.
    Haqiqiy subsistemaga kirish huquqini boshqaradi va kechiktirilgan initsializatsiyani amalga oshiradi.
    """
    
    def __init__(self, real_subsystem):
        self._real_subsystem = real_subsystem
        self._initialized = False
        self._access_count = 0
    
    def initialize(self):
        """Kechiktirilgan initsializatsiya - faqat birinchi marta kirish vaqtida initsializatsiya"""
        if not self._initialized:
            print(f"[PROXY] {self._real_subsystem.get_name()} initsializatsiya qilinyapti...")
            self._real_subsystem.initialize()
            self._initialized = True
        else:
            print(f"[PROXY] {self._real_subsystem.get_name()} allaqachon initsializatsiya qilingan")
    
    def get_status(self) -> dict:
        """Haqiqiy ob'ektga jurnallash bilan kirish"""
        if not self._initialized:
            self.initialize()
        
        self._access_count += 1
        status = self._real_subsystem.get_status()
        status['access_count'] = self._access_count
        return status
    
    def execute_command(self, command: str) -> bool:
        """Kirish nazorati bilan buyruqni bajarish"""
        if not self._initialized:
            self.initialize()
        
        allowed_commands = ['start', 'stop', 'status', 'configure']
        
        if command.lower() not in allowed_commands:
            print(f"[PROXY] Kirish Rad Qilindi: '{command}' buyruqiga ruhsat yo'q")
            return False
        
        print(f"[PROXY] Buyruq bajarilmoqda: {command}")
        return True
    
    def shutdown(self):
        """Haqiqiy subsistemani o'chirish"""
        if self._initialized:
            print(f"[PROXY] {self._real_subsystem.get_name()} o'chirilmoqda...")
            self._real_subsystem.shutdown()
            self._initialized = False


# Eski kod uchun
ISubsystemProxy = ISubsistemProxy
SubsystemProxy = SubsistemProxy
