def forecast(*args):
    result = []
    weather_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for location, weather in args:
        weather_dict[weather].append(location)

    for key, val in weather_dict.items():
        for v in sorted(val):
            result.append(f'{v} - {key}')
    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
