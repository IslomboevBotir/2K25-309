import pytest
from smartcity.controller import CityController

@pytest.fixture
def controller():
    return CityController()