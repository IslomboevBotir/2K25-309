from abc import ABC, abstractmethod



class WeatherInfo:
    def __init__(self, condition: str, temperature: float):
        self.condition = condition
        self.temperature = temperature

class WeatherService(ABC):
    @abstractmethod
    def get_weather(self) -> WeatherInfo:
        pass
    
    
class WeatherProvider:
    def fetch(self):
        return {"condition": "Sunny", "temperature": 26.5, "humidity": 100}


class WeatherAdapter(WeatherService):
    def __init__(self, provider: WeatherProvider):
        self.provider = provider

    def get_weather(self) -> WeatherInfo:
        data = self.provider.fetch()

        return WeatherInfo(
            condition=data.get("condition", "Unknown"),
            temperature=data.get("temperature", 0.0)
        )

