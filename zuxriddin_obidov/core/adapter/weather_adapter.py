class WeatherInfo:
    def __init__(self, condition: str, temperature: float):
        self.condition = condition
        self.temperature = temperature

class WeatherProvider:
    def fetch(self):
        return {"condition": "Sunny", "temperature": 26.5, "humidity": 100}

class WeatherAdapter:
    def __init__(self, provider):
        self.provider = provider

    def get_weather(self) -> WeatherInfo:
        data = self.provider.fetch()
        return WeatherInfo(data["temperature"], data["condition"])
