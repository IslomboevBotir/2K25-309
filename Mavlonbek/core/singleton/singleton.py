# FIO/core/singleton/singleton.py

class Singleton(type):
    """
    Design Pattern: Singleton (Creational)
    Purpose: Ensures a class has only one instance and provides a global point of access to it.
    Usage: Used as a metaclass for the SmartCityController to ensure only one central controller exists.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Make the directory a package
__all__ = ['Singleton']
