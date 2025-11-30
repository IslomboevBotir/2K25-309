from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event: str):
        pass

class EventManager:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, event: str):
        for observer in self._observers:
            observer.update(event)