from smartcity.config import Config

def test_proxy_blocks_wrong_password(capsys, controller):
    controller.access_security_camera("wrong123")
    captured = capsys.readouterr()
    assert "PAROL XATO" in captured.out
    assert "rad etildi" in captured.out

def test_proxy_allows_correct_password(capsys, controller):
    controller.access_security_camera(Config.SECURITY_PASSWORD)
    captured = capsys.readouterr()
    assert "Parol to'g'ri" in captured.out
    assert "jonli efirda" in captured.out or "stream" in captured.out