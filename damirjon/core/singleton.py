# singleton.py
# PATTERN: Singleton – birgina obyekt yaratilishiga ruxsat beradi.

class Singleton(type):
    """Singleton metaclass"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # First time creation
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

