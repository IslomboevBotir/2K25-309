import unittest
from core.event_manager import EventManager, Observer

class FakeObserver(Observer):
    def __init__(self):
        self.events = []

    def update(self, event: str):
        self.events.append(event)

class TestObserver(unittest.TestCase):
    def test_subscribe_and_notify(self):
        manager = EventManager()
        obs = FakeObserver()
        manager.subscribe(obs)
        manager.notify("test_event")
        self.assertIn("test_event", obs.events)

    def test_unsubscribe_works(self):
        manager = EventManager()
        obs = FakeObserver()
        manager.subscribe(obs)
        manager.unsubscribe(obs)
        manager.notify("test_event")
        self.assertNotIn("test_event", obs.events)

    def test_multiple_observers_notified(self):
        manager = EventManager()
        obs1 = FakeObserver()
        obs2 = FakeObserver()
        manager.subscribe(obs1)
        manager.subscribe(obs2)
        manager.notify("alert")
        self.assertIn("alert", obs1.events)
        self.assertIn("alert", obs2.events)