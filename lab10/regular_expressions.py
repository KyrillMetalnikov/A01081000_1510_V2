"""Demonstrate correct usage of regular expressions."""
import re


def is_email(address: str) -> bool:
    """
    Determine if there's an email inside of a string.

    Uses regex search method to see if something matches an email within the text inputted.
    :param address: A string.
    :precondition: address must be inputted as a string.
    :postcondition: Function will determine if there is an email within the string.
    :return: A boolean representing if it found a string or not.

    >>> is_email("Kyrill@hotmail.com")
    True
    >>> is_email("xX_420N008Sn1p3R_Xx@9gag.ca")
    True
    >>> is_email("a;slkdjf;alskdjf;lakjs;lakefj r@d.com asdfasdf")
    True
    >>> is_email(";alskdjf;alkjsdf _@hoSJ ;SLDF.x ")
    False
    """
    email_address_regex = re.compile(r'''(
    (\w+)+  # username part of email
    @  # at symbol separating username from domain
    ([a-z]|\d*)+  # domain name
    [.]+  # period separating domain name with top level domain
    ([a-z]{2,4})  # top level domain
    )''', re.I | re.VERBOSE)
    match_object = email_address_regex.search(address)
    if match_object:
        return True
    else:
        return False


def main():
    print(is_email("Stefan's address is sazaric2@9999.com ya know?"))


if __name__ == "__main__":
    main()
