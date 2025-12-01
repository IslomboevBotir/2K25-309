from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def info(self):
        pass

class LedLight(Device):
    def info(self):
        return 'LED light (energy efficient)'

class HalogenLight(Device):
    def info(self):
        return 'Halogen light (standard)'

class ElectricBus(Device):
    def info(self):
        return 'Electric bus'

class DieselBus(Device):
    def info(self):
        return 'Diesel bus'

class DeviceFactory(ABC):
    @abstractmethod
    def create_light(self):
        pass

    @abstractmethod
    def create_transport_unit(self):
        pass

class EnergySavingFactory(DeviceFactory):
    def create_light(self):
        return LedLight()
    def create_transport_unit(self):
        return ElectricBus()

class StandardFactory(DeviceFactory):
    def create_light(self):
        return HalogenLight()
    def create_transport_unit(self):
        return DieselBus()
