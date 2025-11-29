def test_builder_creates_custom_light():
    from smartcity.builders import StreetLightBuilder

    light = (StreetLightBuilder()
             .set_location("Chorsu")
             .set_brightness(95)
             .with_sensor()
             .set_auto_mode(True)
             .build())

    assert light.location == "Chorsu"
    assert light.brightness == 95
    assert light.sensor is True
    assert light.auto_mode is True