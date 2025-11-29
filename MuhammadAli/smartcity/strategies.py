from abc import ABC, abstractmethod

class TrafficStrategy(ABC):
    @abstractmethod
    def execute(self): pass

class NormalTraffic(TrafficStrategy):
    def execute(self): print("Normal trafik rejimi: 60s yashil")

class RushHourTraffic(TrafficStrategy):
    def execute(self): print("Pik soat: 90s yashil, 10s sariq")

class NightTraffic(TrafficStrategy):
    def execute(self): print("Tunda: 30s yashil, tez o'tish")

class TrafficControlCenter:
    def __init__(self, strategy: TrafficStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TrafficStrategy):
        self.strategy = strategy
        from smartcity.logger import Logger
        Logger().log("INFO", f"Trafik strategiyasi o'zgartirildi: {strategy.__class__.__name__}")

    def run(self):
        print("Svetofor strategiyasi ishga tushdi → ", end="")
        self.strategy.execute()