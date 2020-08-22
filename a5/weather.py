"""Display the daily weather."""
import json
import requests
import datetime


def get_json(url: str) -> dict:
    """
    Get and load the JSON object from url.

    :param url: The url of the json object.
    :precondition: The url will be a valid api address.
    :postcondition: The function will get the json object from the address.
    :return: A dict version of the json object.
    """
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)


def display_weather(api_call: dict, day: int) -> None:
    """
    Display the weather in vancouver for a set amount of days.

    :param api_call: An openweatherapi json object converted to dict.
    :param day: An integer representing how many day to show.
    :precondition: The rules of the param must be followed with days being between 1-8.
    :postcondition: The weather will be displayed.
    """
    display_weather_description(api_call, day)
    display_min_max_temperature(api_call, day)
    display_sunrise_sunset(api_call, day)


def display_weather_description(api_call: dict, day: int) -> None:
    """
    Display the weather description.

    Displays if it is rainy, cloudy etc.
    :param api_call: An openweatherapi json object converted to dict.
    :param day: An integer representing which day to display.
    :precondition: The rules of the param must be followed with day being between 1-8.
    :postcondition: The weather description will be displayed.
    """
    print(api_call["daily"][day]["weather"][0]["main"])


def display_min_max_temperature(api_call: dict, day: int) -> None:
    """
    Display the minimum and maximum temperature.

    :param api_call: An openweatherapi json object converted to dict.
    :param day: An integer representing which day to display.
    :precondition: The rules of the param must be followed with day being between 1-8.
    :postcondition: The minimum and maximum temperatures will be displayed in celcius.
    """
    print(f'Minimum temperature: {api_call["daily"][day]["temp"]["min"]}\n'
          f'Maximum temperature: {api_call["daily"][day]["temp"]["max"]}')


def display_sunrise_sunset(api_call: dict, day: int) -> None:
    """
    Display the time of the sunrise and sunset.

    :param api_call: An openweatherapi json object converted to dict.
    :param day: An integer representing which day to display.
    :precondition: The rules of the param must be followed with day being between 1-8.
    :postcondition: The time of the sunrise and sunset will be displayed.
    """
    print(f'Sunrise: {datetime.datetime.fromtimestamp(api_call["daily"][day]["sunrise"])}\n'
          f'Sunset: {datetime.datetime.fromtimestamp(api_call["daily"][day]["sunset"])}')


def main():
    url = 
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
