from datetime import date
import weather


def display_near_earth_objects_velocity(api_call: dict, day: date):
    print(api_call["near_earth_objects"][str(day)][0]["close_approach_data"][0]
          ["relative_velocity"]["kilometers_per_hour"])


def get_tomorrows_date(todays_date: date):
    todays_date = todays_date.replace(day=(todays_date.day + 1))
    return todays_date


def main():
    todays_date = date.today()
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=&end_date=&api_key=" \
          f"KGgZUIGnLV5bsFf9auZsc7xFdHzgTTkzz5Alq6P8"
    display_near_earth_objects_velocity(weather.get_json(url), get_tomorrows_date(todays_date))


if __name__ == "__main__":
    main()
