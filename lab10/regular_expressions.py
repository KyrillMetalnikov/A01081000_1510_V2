"""Demonstrate correct usage of regular expressions."""
import re


def is_email(address: str) -> bool:
    email_address_regex = re.compile(r'''(
    (\w*)+
    @+
    ([a-z]|\d*)+
    [.]+
    ([a-z]{2,4}))''', re.I | re.VERBOSE)
    match_object = email_address_regex.search(address)
    if match_object:
        print("The email address you entered is: ", match_object.group())
    else:
        print("That's not an email address.")


def main():
    is_email("kmetalnikov@hotmail.com")


if __name__ == "__main__":
    main()
