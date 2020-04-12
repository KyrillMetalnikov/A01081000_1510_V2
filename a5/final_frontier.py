from datetime import date
import weather
import time


def display_near_earth_objects_velocity(api_call: dict, day: date):
    print(f'''The speed of this asteroid is {api_call["near_earth_objects"][str(day)][0]["close_approach_data"][0]
    ["relative_velocity"]["kilometers_per_hour"]} kilometers per hour relative to the earth.\n''')


def display_asteroid_name(api_call: dict, day: date):
    print(f'There is an asteroid named {api_call["near_earth_objects"][str(day)][0]["name"]}.')


def display_asteroid_size(api_call: dict, day: date):
    print(f'''This asteroid is also estimated to be a max of {api_call["near_earth_objects"][str(day)][0]
    ["estimated_diameter"]["meters"]["estimated_diameter_max"]} meters in diameter''')


def get_tomorrows_date(todays_date: date):
    todays_date = todays_date.replace(day=(todays_date.day + 1))
    return todays_date


def main():
    todays_date = date.today()
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=&end_date=&api_key=" \
          f"KGgZUIGnLV5bsFf9auZsc7xFdHzgTTkzz5Alq6P8"
    # for i in range(0, 8):
    #     display_asteroid_name(weather.get_json(url), get_tomorrows_date(todays_date))
    #     display_near_earth_objects_velocity(weather.get_json(url), get_tomorrows_date(todays_date))
    #     todays_date = get_tomorrows_date(todays_date)
    #     time.sleep(300)
    display_asteroid_size(weather.get_json(url), get_tomorrows_date(todays_date))


if __name__ == "__main__":
    main()
