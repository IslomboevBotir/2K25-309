def test_waste_truck_sent_when_full(capsys):
    from modules.waste import WasteManagement
    WasteManagement().check_bins()
    captured = capsys.readouterr()
    assert "Mashina yuborildi" in captured.out