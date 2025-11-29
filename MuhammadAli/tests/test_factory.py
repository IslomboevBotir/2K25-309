def test_factory_creates_correct_types(capsys):
    from smartcity.factories import TransportFactory, LightingFactory, EnergyFactory

    t = TransportFactory().create_system()
    l = LightingFactory().create_system()
    e = EnergyFactory().create_system()

    assert "TransportSystem" in str(type(t))
    assert "LightingSystem" in str(type(l))
    assert "EnergySystem" in str(type(e))

    captured = capsys.readouterr()
    assert "Factory" in captured.out