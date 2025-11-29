import pytest
def test_full_system_integration(capsys, controller):
    controller.manage_transport()
    controller.manage_lighting()
    controller.access_security_camera("smart2025")
    controller.monitor_energy()
    controller.get_weather()
    controller.full_report()

    output = capsys.readouterr().out.lower()

    assert any(word in output for word in ["svetofor", "transport", "trafik"])
    assert any(word in output for word in ["yoritish", "yorug'lik", "brightness", "chiroq"])
    assert "parol to'g'ri" in output or "ochildi" in output
    assert "energiya" in output
    assert "ob-havo" in output or "weather" in output
    assert any(word in output for word in ["hisobot", "report", "smartcity", "to'liq"])