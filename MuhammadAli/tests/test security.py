def test_security_system_has_multiple_cameras():
    from modules.security import AdvancedSecuritySystem
    system = AdvancedSecuritySystem()
    assert len(system.cameras) >= 3
    assert "markaz" in system.cameras