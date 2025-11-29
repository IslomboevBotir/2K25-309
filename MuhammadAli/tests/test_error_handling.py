def test_invalid_traffic_mode_graceful():
    from smartcity.controller import CityController
    ctrl = CityController()
    ctrl.change_traffic_mode("invalid_mode")
