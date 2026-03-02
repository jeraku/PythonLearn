def add(a: int, b: int):
    return a + b


def get_weather(city: str):
    fake_weather = {
        "chennai": "Hot 35°C",
        "bangalore": "Cool 22°C",
        "delhi": "Cold 10°C"
    }
    return fake_weather.get(city.lower(), "Weather not found")