from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, msg: str): pass

class Observable:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, obs): self._observers.append(obs) if obs not in self._observers else None
    def detach(self, obs): self._observers.remove(obs) if obs in self._observers else None
    def notify(self, msg):
        print(f"[Observer] → {msg}")
        for o in self._observers:
            o.update(msg)