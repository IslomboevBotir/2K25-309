"""
Logger implemented as a Singleton.
Used for simple console logging across the app.
"""


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Singleton pattern
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message: str):
        print(f"[LOG] {message}")
