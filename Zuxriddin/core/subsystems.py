from abc import ABC, abstractmethod

# Bridge: Implementation interface
class LightImplementation(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

# Bridge: Abstraction
class LightingSystem(ABC):
    def __init__(self, impl: LightImplementation):
        self.impl = impl

    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
