# SmartCity System — Lab Work №1 (Jamshidbek)

## Run
python Jamshidbek/main.py

## Tests
python Jamshidbek/test.py

## Design Patterns Used
- Singleton — SmartCityController (single instance)
- Facade — SmartCityController provides unified methods for subsystems
- Abstract Factory — DefaultCityFactory creates subsystem objects consistently
- Builder — CityConfigBuilder builds CityConfig step-by-step
- Adapter — WeatherAdapter adapts ExternalWeatherService to internal interface
- Proxy — SecurityProxy controls access to security operations by role
- Decorator — EcoLightingDecorator adds eco brightness cap without changing LightingSystem
