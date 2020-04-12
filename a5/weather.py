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
    print(f"With temperature fluctuations from {api_call['daily'][0]['temp']['min']} C "
          f"to {api_call['daily'][0]['temp']['max']} C")


def display_weather_description(api_call: object, day: int) -> None:
    print(api_call["daily"][day]["weather"][0]["main"])


def main():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=49.2827&lon=123.1207&units=metric&appid"\
          "=7f1f5906c928af9f27256e0472282275"
    display_weather(get_json(url))


if __name__ == "__main__":
    main()
