def test_lighting_adjusts_based_on_weather(monkeypatch, capsys):
    from modules.weather import WeatherSystem
    from modules.lighting import LightingSystem

    def mock_weather(self):
        print("Ob-havo: yomg'irli, 12°C")
        return {"condition": "yomg'irli", "temp": 12}

    monkeypatch.setattr(WeatherSystem, "get_current_weather", mock_weather)

    lighting = LightingSystem()
    weather = WeatherSystem()
    lighting.auto_adjust_with_weather(weather)

    captured = capsys.readouterr()
    assert "100%" in captured.out