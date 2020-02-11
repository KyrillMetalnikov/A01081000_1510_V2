import random


def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate a dice roll.

    :param number_of_sides: A positive non-zero integer representing the number of sides on the dice.
    :param number_of_rolls: A positive non-zero integer representing the number of rolls.
    :precondition: Both parameters are non-zero positive integers.
    :postcondition: An accurate dice roll will be simulated.
    :return: The total value of the dice roll
    """
    total_roll = 0
    for i in range(0, number_of_rolls):
        total_roll += random.randint(1, number_of_sides + 1)
    return total_roll


def generate_name(syllables):
    """
    Create a random name.

    :param syllables: A positive non-zero integer representing the number of syllables in the random name.
    :precondition: The rules of the parameter are followed.
    :postcondition: A random name of specified syllables will be created.
    :return: Returns a string representing a random name.
    """
    name = ""
    for i in range(0, syllables + 1):
        name += generate_syllable()
    return name



def generate_vowel():
    """
    Generate a random vowel.

    :precondition: Provide the function with no inputs.
    :postcondition: Function will create a single random vowel.
    :return: A vowel in string format.
    """
    return random.choice("aeiouy")


def generate_consonant():
    """
    Generate a random consonant.

    :precondition: Provide the function with no inputs.
    :postcondition: Function will create a single random consonant.
    :return: A consonant in in string format.
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_syllable():
    """
    Generate a random syllable of one consonant and one vowel.

    :precondition: Provide no inputs into the function.
    :postcondition: Function will create a single random syllable.
    :return: A two character syllable in string format.
    """

    return (generate_consonant() + generate_vowel()).join()