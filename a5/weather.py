"""Display the daily weather."""
import json
import requests
# key = 7f1f5906c928af9f27256e0472282275
# url=https://api.openweathermap.org/data/2.5/onecall?lat=49.2827&lon=123.1207&unit=metric&appid=


def get_forecast(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)
    print(vancouver_weather["current"])


def main():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=49.2827&lon=123.1207&unit=metric&appid"\
          "=7f1f5906c928af9f27256e0472282275"
    get_forecast(url)


if __name__ == "__main__":
    main()