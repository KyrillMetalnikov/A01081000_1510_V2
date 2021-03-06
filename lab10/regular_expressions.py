"""Demonstrate correct usage of regular expressions."""
import re
import doctest


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
    False
    >>> is_email(";alskdjf;alkjsdf _@hoSJ ;SLDF.x ")
    False
    """
    email_address_regex = re.compile(r'''(^
    \w+  # username part of email
    @  # at symbol separating username from domain
    [a-z\d]+  # domain name
    \.([a-z]){2,4}  # top level domain
    $)''', re.I | re.VERBOSE)
    match_object = email_address_regex.search(address)
    if match_object:
        return True
    else:
        return False


def is_nakamoto(name):
    """
    Determine if the name inputted is a full name with Nakamoto as the last name.

    :param name: A string
    :precondition: name must be a string.
    :postcondition: Function will determine if there is a name XXX Nakamoto in the string.
    :return: A boolean representing whether or not there is the name within the string.

    >>> is_nakamoto("Charles Nakamoto")
    True
    >>> is_nakamoto("charles Nakamoto")
    False
    >>> is_nakamoto("Charles nakamoto")
    False
    >>> is_nakamoto("s;dfsjdkfl Charles Nakamoto fhalwkfhaks")
    False
    """
    full_name_of_nakamoto_regex = re.compile(r'''(^
    [A-Z][a-z]+  # Firstname must be a capital letter followed by lowercase letters
    [ ]  # 
    Nakamoto
    $)''', re.VERBOSE)
    match_object = full_name_of_nakamoto_regex.search(name)
    if match_object:
        return True
    else:
        return False


def is_poker(hand):
    """
    Determine if the hand is a valid poker hand.

    Function checks if all characters can be valid cards, and makes sure there isn't more than 4 of the same card.
    :param hand: Hand is a string representing a potential poker hand.
    :precondition: hand must be a string.
    :postcondition: Function will check if it's a valid poker hand.
    :return: A boolean representing if it was a valid hand.
    >>> is_poker("12345")
    False
    >>> is_poker("qkkkq")
    True
    >>> is_poker("5678")
    False
    >>> is_poker("jkqa88")
    False
    """
    # checks the hands for valid characters and length
    poker_hand_regex_characters = re.compile(r'^((([ajqkt])|([2-9])){5})$', re.I | re.VERBOSE)
    match_object = poker_hand_regex_characters.search(hand)
    poker_hand_regex_valid = re.compile(r'(\w)\1{4}')  # checks to see if it's a 5 of a kind
    five_of_a_kind = poker_hand_regex_valid.search(hand)
    if match_object and not five_of_a_kind:  # not 5 of a kind as that's an invalid hand.
        return True
    else:
        return False


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
