"""
Contain and run a variety of different functions and their helpers.
"""
import math
import random
import doctest


def convert_to_roman_numeral(positive_int):
    """
    Convert a number to roman numerals then print it out.

    Uses a variety of helper functions to convert a number between 1-10000 to roman numerals then prints it on screen.
    For this function I used decomposition by splitting the function into a few separate functions.  I also used pattern
    matching by reusing structures with only different parameters in order to save space.
    :param positive_int: The number being converted to roman numerals: type int
    :precondition: Input an integer between 1-10000
    :postcondition: The correct roman numeral will be displayed on screen
    :return: no return

    >>> convert_to_roman_numeral(5)
    '5 in roman numerals is V'
    >>> convert_to_roman_numeral(50)
    '50 in roman numerals is L'
    >>> convert_to_roman_numeral(785)
    '785 in roman numerals is DCCLXXXV'
    >>> convert_to_roman_numeral(3579)
    '3579 in roman numerals is MMMDLXXIX'
    >>> convert_to_roman_numeral(10000)
    '10000 in roman numerals is MMMMMMMMMM'
    """

    positive_int = str(positive_int)
    if len(positive_int) == 5:
        return positive_int + " in roman numerals is MMMMMMMMMM"
    elif len(positive_int) == 4:  # used if the number's between 1000-9999
        return (positive_int + " in roman numerals is " + "M" * int(separate_chars(positive_int)[0])
                + str(find_roman_digit(separate_chars(positive_int)[1], "C", "D", "M"))
                + str(find_roman_digit(separate_chars(positive_int)[2], "X", "L", "C"))
                + str(find_roman_digit(separate_chars(positive_int)[3], "I", "V", "X")))
    elif len(positive_int) == 3:  # used if the number's between 100-999
        return (positive_int + " in roman numerals is "
                + str(find_roman_digit(separate_chars(positive_int)[0], "C", "D", "M"))
                + str(find_roman_digit(separate_chars(positive_int)[1], "X", "L", "C"))
                + str(find_roman_digit(separate_chars(positive_int)[2], "I", "V", "X")))
    elif len(positive_int) == 2:  # used if the number's between 10-99
        return (positive_int + " in roman numerals is "
                + str(find_roman_digit(separate_chars(positive_int)[0], "X", "L", "C"))
                + str(find_roman_digit(separate_chars(positive_int)[1], "I", "V", "X")))
    elif len(positive_int) == 1:  # used if the number's between 1 - 9
        return (positive_int + " in roman numerals is "
                + find_roman_digit(separate_chars(positive_int)[0], "I", "V", "X"))


def find_roman_digit(digit, ones, fives, tens):
    """
    Convert a digit to roman numerals.

    Convert a digit to roman numerals based on symbols inserted.
    :param digit: The digit to be converted: type integer
    :param ones: The ones place for the roman conversion: type string
    :param fives: The fives place for the roman conversion: type string
    :param tens: The tens place for the roman conversion: type string
    :precondition: The digit must be an integer from 1-9 and the other 3 params must be single value Roman chars
    :postcondition: Will return the correct roman numeral
    :return: The roman numeral of the digit inputted: type string

    >>> find_roman_digit(5,"I", "V", "X")
    'V'
    >>> find_roman_digit(3, "X", "L", "C")
    'XXX'
    >>> find_roman_digit(9, "C", "D", "M")
    'CM'
    """
    digit = int(digit)
    if 1 <= digit <= 3:
        return ones * digit
    elif digit == 4:
        return ones + fives
    elif 5 <= digit <= 8:
        return fives + (digit - 5) * ones
    elif digit == 9:
        return ones + tens
    else:
        return ""


def colour_mixer():
    """
    Mix two primary colours together.

    User inputs two primary colours and the function displays what colour is created when the two colours are mixed.
    I used pattern matching to organize the code as the if statements are almost identical so i can group them
    together.
    :precondition: Each input must be a primary colour (red, yellow, blue) and both inputs have to be different colours.
    :postcondition: Function will display the mixed colour.
    :return: no return
    """
    print("Hello!  Please input two different primary colours and we will mix them for you!")
    two_colours = [input("Please enter your first primary colour!").strip().lower(),
                   input("Thank you, now please enter your second primary colour!").strip().lower()]

    if "red" in two_colours and "yellow" in two_colours:
        print("You have created orange!")
    elif "red" in two_colours and "blue" in two_colours:
        print("You have created purple!")
    elif "yellow" in two_colours and "blue" in two_colours:
        print("You have created green!")
    else:
        print("error: Please input two different primary colours for me to mix (red, yellow, or blue")


def time_calculator(seconds):
    """
    Print how many days, hours, minutes and seconds there are in a certain number of seconds.

    I used pattern matching in this program as it is the same sequence of math operations just with a different
    denominator.  I also used the algorithm of doing days, hours, minutes, and then seconds as that makes the function
    be able to take any positive integer value and still be able to provide an accurate output.
    :param seconds: A positive integer that represents an amount of seconds
    :precondition: Number must be a positive integer
    :postcondition: Calculates how many days, hours, minutes and seconds there are in that number.
    :return: no return
    >>> time_calculator(86400)
    1 0 0 0
    >>> time_calculator(100000)
    1 3 46 40
    >>> time_calculator(0)
    0 0 0 0
    """
    time_in_days = str(math.floor(seconds / 86400))  # inputted number's divided by seconds in a day
    new_seconds = seconds % 86400  # removes the seconds used when finding number of days
    time_in_hours = str(math.floor(new_seconds / 3600))  # inputted number's divided by seconds in an hour
    new_seconds = new_seconds % 3600
    time_in_minutes = str(math.floor(new_seconds / 60))  # inputted number's divided by seconds in a minute
    time_in_seconds = str(new_seconds % 60)
    print(time_in_days + " " + time_in_hours + " " + time_in_minutes + " " + time_in_seconds)


def compound_interest(principal, annual_interest_rate, number_of_yearly_compounds, number_of_years_held):
    """
    Return how much money I will have after my interest compounds.

    Uses the compound interest formula to calculate how much money will be had after acquiring interest for a set time.

    I used the algorithm a= p(1+i/n)^nt to find how much money would be in an account after acquiring interest for a set
    period of time.
    :param principal: The amount of money that was originally deposited into the account: type float
    :param annual_interest_rate: The amount of yearly interest made on that account: type float
    :param number_of_yearly_compounds: The amount of times the interest compounds per year: type int
    :param number_of_years_held: The amount of years the money is held for: type float
    :precondition: User will input positive non-zero numbers
    :postcondition: Function will properly do the calculation
    :return: The amount of money in the account after the interest is compounded: type float
    >>> compound_interest(10000, 0.1, 12, 5)
    16453.089347785855
    >>> compound_interest(5000, 0.05, 24, 0.5)
    5126.44228491645
    """
    return (principal * ((1 + (annual_interest_rate / number_of_yearly_compounds))  # formula for compound interest
            ** (number_of_yearly_compounds * number_of_years_held)))  # second part of formula


def rock_paper_scissors():
    """
    Play a round of rock, paper, scissors.

    I pattern matched all the blocks of code together, as the only difference between them is the possible outputs.
    :precondition: You will only input either "rock", "paper" or "scissors"
    :postcondition:  You will experience a game of rock paper scissors.
    :return: no return
    """
    list_of_options = ["rock", "paper", "scissors"]
    computers_choice = random.choice(list_of_options)
    print("Hello!  Let's play a round of rock, paper, scissors!")
    user_input = input("What is your choice: rock, paper, or scissors?").strip().lower()

    if user_input == "rock":
        if computers_choice == "paper":
            print("You picked " + user_input + " and your opponent picked " + computers_choice + ".  You lose!")
        elif computers_choice == "scissors":
            print("You picked " + user_input + " and your opponent picked " + computers_choice + ".  You win!")

    if user_input == "paper":
        if computers_choice == "rock":
            print("You picked " + user_input + " and your opponent picked " + computers_choice + ".  You win!")
        elif computers_choice == "scissors":
            print("You picked " + user_input + " and your opponent picked " + computers_choice + ".  You lose!")

    if user_input == "scissors":
        if computers_choice == "rock":
            print("You picked " + user_input + " and your opponent picked " + computers_choice + ".  You lose!")
        elif computers_choice == "paper":
            print("You picked " + user_input + " and your opponent picked " + computers_choice + ".  You win!")

    if user_input == computers_choice:
        print("You and your opponent both picked " + user_input + ".  You tied!")


def number_generator():
    """
    Generate a list of random numbers.

    I decomposed this function by spreading out what I needed to do.  I first make a list of possible numbers, then
    I randomly pick from those numbers, and then I sort them from smallest to greatest instead of doing it all in go.
    I haven't used abstraction for this function as that didn't fit the requirement, but I can see how I could make this
    work as a random number generator for any size numbers and as many random numbers as the computer can hold.
    :precondition: Don't write any parameters.
    :postcondition: You will get 6 random unique numbers from 1-49
    :return: returns a list of random unique integers
    """
    list_of_numbers = []
    for i in range(1, 49):
        list_of_numbers.append(i + 1)
    draw = random.sample(list_of_numbers, 6)
    return sorted(draw)


def number_translator():
    """
    Convert letters in a phone number to numbers.

    I used pattern recognition as the if statement repeated in the same pattern so i grouped them all in blocks.  I also
    used decomposition as I used a helper function to separate the characters in the phone number.
    :precondition: You will input a 10 digit phone number formatted XXX-XXX-XXXX
    :postcondition: YOu will receive a phone numbers with only numbers and dashes
    :return: The new phone number with no letters: type string
    """
    print("Hello!  Please enter your phone number and we will convert all letters to numbers!")
    phone_number_raw = input("Please input your phone number in the form XXX-XXX-XXXX").lower()
    phone_number = separate_chars(phone_number_raw)  # use helper function to convert input into a list of chars

    for char in range(12):  # range is 12 as we need 12 characters
        if isinstance(phone_number[char], int):  # checking if the element is a number
            pass

        elif phone_number[char] == "-":
            pass

        else:
            if phone_number[char] == "a" or phone_number[char] == "b" or phone_number[char] == "c":
                phone_number[char] = "2"

            elif phone_number[char] == "d" or phone_number[char] == "e" or phone_number[char] == "f":
                phone_number[char] = "3"

            elif phone_number[char] == "g" or phone_number[char] == "h" or phone_number[char] == "i":
                phone_number[char] = "4"

            elif phone_number[char] == "j" or phone_number[char] == "k" or phone_number[char] == "l":
                phone_number[char] = "5"

            elif phone_number[char] == "m" or phone_number[char] == "n" or phone_number[char] == "o":
                phone_number[char] = "6"

            elif phone_number[char] == "p" or phone_number[char] == "q" or phone_number[char] == "r" \
                    or phone_number[char] == "s":

                phone_number[char] = "7"

            elif phone_number[char] == "t" or phone_number[char] == "u" or phone_number[char] == "v":
                phone_number[char] = "8"

            elif phone_number[char] == "w" or phone_number[char] == "x" or phone_number[char] == "y" \
                    or phone_number[char] == "z":
                phone_number[char] = "9"

    return "".join(phone_number)


def separate_chars(string_of_chars):
    """
    Convert a string into a list of separate characters.

    :param string_of_chars: The grouping of characters to separate. Type: all types
    :precondition: You must input at least one character
    :postcondition: Will output a list of separate characters
    :return: returns list of each character separated
    >>> separate_chars("wagu beef")
    ['w', 'a', 'g', 'u', ' ', 'b', 'e', 'e', 'f']
    >>> separate_chars("Kyrill")
    ['K', 'y', 'r', 'i', 'l', 'l']
    >>> separate_chars("E")
    ['E']
    """
    list_of_chars = []

    for i in str(string_of_chars):
        list_of_chars.append(i)
    return list_of_chars


def main():
    """
    Run all the functions in this module.

    :return: no return
    """
    # convert_to_roman_numeral(5)
    # convert_to_roman_numeral(3579)
    # colour_mixer()
    # time_calculator(70)
    # print(compound_interest(5000, 0.05, 24, 0.5))
    # rock_paper_scissors()
    print(number_generator())
    # print(number_translator())


if __name__ == "__main__":
    doctest.testmod()
    main()
