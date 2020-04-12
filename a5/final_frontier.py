import json
import requests
import weather


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


def main():
    url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=KGgZUIGnLV5bsFf9auZsc7x" \
          "FdHzgTTkzz5Alq6P8"
    print(get_json(url))
