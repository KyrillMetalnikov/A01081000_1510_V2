"""Display the daily weather."""
import json
import requests
import datetime


def get_json(url: str) -> object:
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)


def display_weather(api_call: object, day: int) -> None:
    display_weather_description(api_call, day)
    display_min_max_temperature(api_call, day)
    display_sunrise_sunset(api_call, day)


def display_weather_description(api_call: object, day: int) -> None:
    print(api_call["daily"][day]["weather"][0]["main"])


def display_min_max_temperature(api_call: object, day: int) -> None:
    print(f'Minimum temperature: {api_call["daily"][day]["temp"]["min"]}\n'
          f'Maximum temperature: {api_call["daily"][day]["temp"]["max"]}')


def display_sunrise_sunset(api_call: object, day: int) -> None:
    print(f'Sunrise: {datetime.datetime.fromtimestamp(api_call["daily"][day]["sunrise"])}\n'
          f'Sunset: {datetime.datetime.fromtimestamp(api_call["daily"][day]["sunset"])}')


def main():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=49.2497&lon=-123.1193&units=metric&appid"\
          "=7f1f5906c928af9f27256e0472282275"
    amount_of_days = input("How many days do you want to see? (up to 7 days)")
    try:
        for day in range(0, int(amount_of_days)):
            if day == 0:
                print("\nToday's weather:\n")
            else:
                print(f"\nDay {day + 1}'s weather:\n")
            display_weather(get_json(url), day)
    except IndexError:
        print("Sorry, I cannot display more than 8 days of weather.")
    if int(amount_of_days) < 1:
        print("I cannot show the weather of 0 or less days!")


if __name__ == "__main__":
    main()
