def test_observer_gets_notified_on_critical_energy(capsys):
    from modules.energy import EnergySystem
    from modules.notification_center import NotificationCenter, MobileApp

    energy = EnergySystem()
    energy.attach(NotificationCenter())
    energy.attach(MobileApp())

    energy.consumption = 750
    energy.notify("TEST: Energiya oshdi")

    captured = capsys.readouterr()
    assert "Markaz:" in captured.out
    assert "Telefon:" in captured.out
    assert "TEST: Energiya oshdi" in captured.out