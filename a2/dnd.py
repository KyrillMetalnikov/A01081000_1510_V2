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
    for i in range(0, syllables + 1):


def generate_vowel():
    """
    Generate a random vowel.
    :precondition: Provide the function with no inputs.
    :postcondition: Will create a single random vowel.
    :return: A vowel in
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return random.choice(vowels)

