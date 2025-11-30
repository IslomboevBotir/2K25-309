# test.py
from modules.lighting import LightingSystem
from modules.security import SecurityProxy
from modules.transport import TransportSystem, HeavyTrafficStrategy

# Test 1: Lighting adapter mavjudligi
def test_lighting_adapter():
    ls = LightingSystem()
    assert hasattr(ls.adapter, "turn_on")

# Test 2: Security proxy authorization
def test_security_proxy():
    proxy = SecurityProxy()
    proxy.authenticate("admin123")
    assert proxy.authorized is True

# Test 3: Transport strategy switching
def test_transport_strategy():
    ts = TransportSystem()
    ts.set_strategy(HeavyTrafficStrategy())
    assert isinstance(ts.strategy, HeavyTrafficStrategy)
