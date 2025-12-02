from abc import ABC, abstractmethod
from .vehicles import Bus, Tram

class TransportSystem(ABC):
    @abstractmethod
    def start_service(self):
        pass
    @abstractmethod
    def stop_service(self):
        pass

class BusSystem(TransportSystem):
    def start_service(self):
        Bus().start()
    def stop_service(self):
        Bus().stop()

class TramSystem(TransportSystem):
    def start_service(self):
        Tram().start()
    def stop_service(self):
        Tram().stop()

class TransportSystemFactory:
    """Factory Method: Delegates vehicle creation to subclasses."""
    @staticmethod
    def create_system(transport_type="bus"):
        if transport_type == "bus":
            return BusSystem()
        elif transport_type == "tram":
            return TramSystem()
        else:
            return BusSystem()  # default