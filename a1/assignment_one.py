import math
import random
import doctest


def find_roman_digit(digit, ones, fives, tens):
    """
    Convert a digit to roman numerals.

    convert a digit to roman numerals based on symbols inserted
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


def separate_chars(string_of_chars):
    """
    Convert a string into a list of separate characters.

    :param string_of_chars: The grouping of characters to separate. Type: all types
    :precondition: You must input at least one character
    :postcondition: Will output a list of separate characters
    :return: returns list of each character separated
    """
    list_of_chars = []

    for x in str(string_of_chars):
        list_of_chars.append(x)
    return list_of_chars


def convert_to_roman_numeral(positive_int):
    """
    Convert a number to roman numerals then print it out.

    Uses a variety of helper functions to convert a number between 1-10000 to roman numerals then prints it on screen
    :param positive_int: The number being converted to roman numerals: type int
    :precondition: Input an integer between 1-10000
    :postcondition: The correct roman numeral will be displayed on screen
    :return: no return

    >>> convert_to_roman_numeral(5)
    5 in roman numerals is V
    >>> convert_to_roman_numeral(50)
    50 in roman numerals is L
    >>> convert_to_roman_numeral(785)
    785 in roman numerals is DCCLXXXV
    >>> convert_to_roman_numeral(3579)
    3579 in roman numerals is MMMDLXXIX
    >>> convert_to_roman_numeral(10000)
    10000 in roman numerals is MMMMMMMMMM
    """

    positive_int = str(positive_int)
    if len(positive_int) == 5:
        print(positive_int + " in roman numerals is MMMMMMMMMM")
    elif len(positive_int) == 4:  # used if the number's between 1000-9999
        print(positive_int + " in roman numerals is " + "M" * int(separate_chars(positive_int)[0])
              + str(find_roman_digit(separate_chars(positive_int)[1], "C", "D", "M"))
              + str(find_roman_digit(separate_chars(positive_int)[2], "X", "L", "C"))
              + str(find_roman_digit(separate_chars(positive_int)[3], "I", "V", "X")))
    elif len(positive_int) == 3:  # used if the number's between 100-999
        print(positive_int + " in roman numerals is "
              + str(find_roman_digit(separate_chars(positive_int)[0], "C", "D", "M"))
              + str(find_roman_digit(separate_chars(positive_int)[1], "X", "L", "C"))
              + str(find_roman_digit(separate_chars(positive_int)[2], "I", "V", "X")))
    elif len(positive_int) == 2:  # used if the number's between 10-99
        print(positive_int + " in roman numerals is "
              + str(find_roman_digit(separate_chars(positive_int)[0], "X", "L", "C"))
              + str(find_roman_digit(separate_chars(positive_int)[1], "I", "V", "X")))
    elif len(positive_int) == 1:  # used if the number's between 1 - 9
        print(positive_int + " in roman numerals is "
              + find_roman_digit(separate_chars(positive_int)[0], "I", "V", "X"))


def colour_mixer():
    """
    Mix two primary colours together.

    User inputs two primary colours and the function displays what colour is created when the two colours are mixed.
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
        print("error: Please input two different primary colours for me to mix")


def time_calculator(seconds):
    """
    Print how many days, hours, minutes and seconds there are in a certain number of seconds.

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
    amount = principal * ((1 + (annual_interest_rate / number_of_yearly_compounds))  # formula for compound interest
                          ** (number_of_yearly_compounds * number_of_years_held))  # second part of formula
    return amount


def rock_paper_scissors():
    """
    Play a round of rock, paper, scissors.

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
    Make a lottery ticket with six unique numbers between 1 and 49.

    :return: returns a list of six unique numbers between 1 and 49.
    """
    lottery_numbers = []
    for x in range(49):
        lottery_numbers.append(x + 1)
    draw = random.sample(lottery_numbers, 6)
    return sorted(draw)


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


if __name__ == "__main__":
    doctest.testmod()
    main()
