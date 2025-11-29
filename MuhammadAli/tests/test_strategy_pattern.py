def test_strategy_pattern_switches_modes(capsys):
    from smartcity.controller import CityController
    ctrl = CityController()
    ctrl.change_traffic_mode("rush")
    ctrl.change_traffic_mode("night")
    captured = capsys.readouterr()
    assert "Pik soat" in captured.out
    assert "Tunda" in captured.out
    assert "strategiyasi o'zgartirildi" in captured.out