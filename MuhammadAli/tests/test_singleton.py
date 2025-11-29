def test_singleton_returns_same_instance():
    from smartcity.controller import CityController
    c1 = CityController()
    c2 = CityController()
    assert c1 is c2
    assert id(c1) == id(c2)