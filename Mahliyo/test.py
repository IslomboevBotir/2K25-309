import pytest

from core.controller import SmartCityController

from core.factories.transport_factory import TransportFactory
from core.factories.lighting_factory import LightingFactory

from modules.transport.bus import Bus
from modules.lighting.street_light import StreetLight
from modules.security.camera import SecurityCamera
from modules.energy.energy_monitor import EnergyMonitor

from core.adapters.weather_adapter import WeatherAdapter
from core.proxy.security_proxy import SecurityProxy


def test_singleton_controller():
    controller1 = SmartCityController()
    controller2 = SmartCityController()

    assert controller1 is controller2


def test_transport_factory_creates_bus():
    factory = TransportFactory()
    transport = factory.create_transport("bus")

    assert isinstance(transport, Bus)


def test_lighting_factory_creates_street_light():
    factory = LightingFactory()
    light = factory.create_light("street")

    assert isinstance(light, StreetLight)


def test_facade_turns_on_all_systems():
    controller = SmartCityController()
    result = controller.start_city()

    assert result is True


def test_weather_adapter_returns_temperature():
    adapter = WeatherAdapter()
    temperature = adapter.get_temperature()

    assert isinstance(temperature, (int, float))


def test_security_proxy_access():
    camera = SecurityCamera()
    proxy = SecurityProxy(camera)
    result = proxy.activate()

    assert result is True


def test_energy_monitor_builder():
    monitor = EnergyMonitor.builder() \
        .set_sensor_count(5) \
        .enable_auto_save() \
        .build()

    assert monitor.sensor_count == 5
    assert monitor.auto_save is True


def test_full_smart_city_workflow():
    controller = SmartCityController()

    controller.start_city()
    controller.enable_security()
    controller.enable_lighting()
    controller.enable_transport()

    status = controller.get_status()

    assert status["city"] == "running"
    assert status["security"] is True
    assert status["lighting"] is True
    assert status["transport"] is True
