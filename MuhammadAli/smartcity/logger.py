# smartcity/logger.py
import datetime
import os

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, level: str, message: str):
        if os.environ.get("SMARTCITY_SILENT") == "1":
            return
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{level.upper()}] {message}")