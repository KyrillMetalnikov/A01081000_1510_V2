from datetime import date
import weather


def display_near_earth_objects(api_call: dict, day: object):
    print(api_call["near_earth_objects"][str(day)])


def get_tomorrows_date():
    todays_date = date.today()
    todays_date = todays_date.replace(day=(todays_date.day + 1))
    return todays_date


def main():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=&end_date=&api_key=" \
          f"KGgZUIGnLV5bsFf9auZsc7xFdHzgTTkzz5Alq6P8"
    display_near_earth_objects(weather.get_json(url), get_tomorrows_date())


if __name__ == "__main__":
    main()
