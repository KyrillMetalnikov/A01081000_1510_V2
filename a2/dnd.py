"""Create an iteration of a DND game."""
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


def create_character(syllables):
    """
    Create a Dungeons and Dragons Character.

    Creates a character by randomly generating a name, randomly generating the 6 core stats, adding an empty inventory,
    setting the race, setting the class, adding an xp counter that starts at 0, and setting the max hp.
    :param syllables: A positive integer representing the number of syllables in the name.
    :precondition: Syllables must be a positive integer.
    :postcondition: A randomized character will be created.
    :return: Returns a dictionary with the character information.
    """
    if type(syllables) != int or syllables < 1:
        print("Error: Please make sure you're only inputting a positive integer.")
        return None
    else:
        character = {"Name": generate_name(syllables),
                     "Strength": roll_die(3, 6),
                     "Dexterity": roll_die(3, 6),
                     "Intelligence": roll_die(3, 6),
                     "Charisma": roll_die(3, 6),
                     "Wisdom": roll_die(3, 6),
                     "Constitution": roll_die(3, 6),
                     "Inventory": [],
                     "XP": 0,
                     "Class": select_class(),
                     "Race": select_race()}

        max_health = set_hitpoints(character)
        current_health = max_health
        character["HP"] = [max_health, current_health]
        return character


def select_class():
    """
    Display all dnd classes, then let user pick a class.

    :precondition: User will only input integers between 1-12 inclusive
    :postcondition: The function will return the name of the corresponding class.
    :return: Name of the class in string format.
    """
    classes = {1: "barbarian",
               2: "bard",
               3: "cleric",
               4: "druid",
               5: "fighter",
               6: "monk",
               7: "paladin",
               8: "ranger",
               9: "rogue",
               10: "sorcerer",
               11: "warlock",
               12: "wizard"}

    for key, value in classes.items():
        print(key, value)

    user_input = int(input("Please input the number of the class you wish to play!"))
    return classes[user_input]


def select_race():
    """
    Display all dnd races, then let user pick a race.

    :precondition: User will only input integers between 1-9 inclusive.
    :postcondition: The function will return the name of the corresponding race
    :return: Name of the race in string format.
    """

    races = {1: "dragonborn",
             2: "dwarf",
             3: "elf",
             4: "gnome",
             5: "half-elf",
             6: "halfling",
             7: "half-orc",
             8: "human",
             9: "tiefling"}

    for key, value in races.items():
        print(key, value)

    user_input = int(input("Please input the number of the race you wish to play!"))
    return races[user_input]


def set_hitpoints(character):
    """
    Set the hitpoints of a character.

    Sets the hitpoints of a character based on the value of hit
    """
    if character["Race"] == "barbarian":
        return roll_die(1, 12)  # Roll a 12 sided die to set hitpoints.
    elif character["Race"] == "fighter" or character["Race"] == "paladin" or character["Race"] == "ranger":
        return roll_die(1, 10)  # roll a 10 sided die to set hitpoints.
    elif character["Race"] == "sorcerer" or character["Race"] == "wizard":
        return roll_die(1, 6)  # roll a 6 sided die to set hitpoints.
    else:
        return roll_die(1, 8)  # Only other value left to set hitpoints with.


def main():
    print(select_race())


if __name__ == "__main__":
    main()
