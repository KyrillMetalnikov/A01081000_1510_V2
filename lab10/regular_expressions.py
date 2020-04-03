"""Demonstrate correct usage of regular expressions."""
import re


def is_email(address: str) -> bool:
    email_address_regex = re.compile(r'''(
    (\w+)+  # username part of email
    @  # at symbol separating username from domain
    ([a-z]|\d*)+  # domain name
    [.]+  # period separating domain name with top level domain
    ([a-z]{2,4})  # top level domain
    )''', re.I | re.VERBOSE)
    match_object = email_address_regex.search(address)
    if match_object:
        print("The email address you entered is: ", match_object.group())
    else:
        print("That's not an email address.")


def main():
    is_email("Stefan's address is sazaric2@g9mail.com ya know?")


if __name__ == "__main__":
    main()
