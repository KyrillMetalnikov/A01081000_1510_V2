"""Display the daily weather."""
import json
import requests
# key = 7f1f5906c928af9f27256e0472282275
# url=https://api.openweathermap.org/data/2.5/onecall?lat=49.2827&lon=123.1207&unit=metric&appid=


def get_json(url: str) -> object:
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)


def display_weather(api_call: object) -> None:
    print("Today the weather will be ", end="")
    display_weather_description(api_call, 0)
    display_min_max_temperature(api_call, 0)


def display_weather_description(api_call: object, day: int) -> None:
    print(api_call["daily"][day]["weather"][0]["main"])


def display_min_max_temperature(api_call: object, day: int) -> None:
    print(f'Minimum temperature: {api_call["daily"][day]["temp"]["min"]}\n'
          f'Maximum temperature: {api_call["daily"][day]["temp"]["max"]}')


def display_sunrise_sunset(api_call: object, day: int) -> None:
    print(f'Sunrise: {api_call["daily"][day]["sunrise"]}\n'
          f'Sunset: {api_call["daily"][day]["sunset"]}')

def main():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=49.2827&lon=123.1207&units=metric&appid"\
          "=7f1f5906c928af9f27256e0472282275"
    display_weather(get_json(url))


if __name__ == "__main__":
    main()
