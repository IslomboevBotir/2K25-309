"""
Singleton Naqshi Implementatsiyasi
Foydalanish: SmartCity Kontrolerining yagona instansiyasini ta'minlash
"""

from abc import ABC, abstractmethod
from typing import Optional


class Singleton(ABC):
    """
    Singleton Naqshi - Klassning faqat bitta instansiyasini ta'minlaydi
    va unga global kirish nuqtasini taqdim etadi.
    """
    _instances = {}  # Klass bo'yicha instansiyalarni saqlash lug'ati

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    @abstractmethod
    def initialize(self):
        """Singleton instansiyasini initsializatsiya qilish"""
        pass

