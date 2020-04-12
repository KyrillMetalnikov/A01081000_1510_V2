import json
import requests
import time
import weather


def main():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=&end_date=&api_key=" \
          f"KGgZUIGnLV5bsFf9auZsc7xFdHzgTTkzz5Alq6P8"
    print(weather.get_json(url))


if __name__ == "__main__":
    main()