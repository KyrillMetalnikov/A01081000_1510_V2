import random
import string
"""
Create a random name and simulate a dice roll
"""


def roll_die(number_of_rolls, number_of_sides):
    """
    simulate dice rolls of inputed sides.

    randomly generates numbers based on the users input of number of rolls and number of sides using random function

    :param number_of_rolls: number of rolls user wants : type int
    :param number_of_sides: number of sides on the die : type int
    :return: returns an integer of the random roll
    """
    if number_of_rolls <= 1 or number_of_sides <= 2:
        return 0
    else:
        return random.randint(number_of_rolls, number_of_rolls * number_of_sides)


def create_name(length):
    """
    Create a random name of inputed length.

    Creates a random name by making a list of ascii characters then joining them together into a string in title case
    :param length: the number of characters the name will be: type integer
    :return: returns the random name in title case: type String
    """
    name = random.choices(string.ascii_letters, k=length)
    return "".join(name).title()


if __name__ == "__main__":
    """
    Main function to test other functions.
    """
    # rolls = int(input("How many dice do you want to roll?"))
    # sides = int(input("How many sides do your dice have?"))
    # print(roll_die(rolls, sides))
    print("Your random name is " + create_name(7))
