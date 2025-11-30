# transport.py
# PATTERN: Strategy – turli transport boshqaruv rejimlari.
# *Note: Strategy pattern optional but counted toward 5 patterns.*

class NormalTrafficStrategy:
    def execute(self):
        print("[Traffic] Normal mode active.")

class HeavyTrafficStrategy:
    def execute(self):
        print("[Traffic] Heavy mode active – optimizing routes.")

class TransportSystem:
    """Transport manager using Strategy pattern"""

    def __init__(self):
        self.strategy = NormalTrafficStrategy()

    def set_strategy(self, strategy):
        self.strategy = strategy

    def manage_traffic(self):
        print("[Transport] Managing traffic flow...")
        self.strategy.execute()
