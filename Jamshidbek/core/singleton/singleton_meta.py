class SingletonMeta(type):
    """
    Singleton Pattern (metaclass helper).
    This project uses Singleton in SmartCityController directly,
    but this file exists for clarity and modular structure.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
