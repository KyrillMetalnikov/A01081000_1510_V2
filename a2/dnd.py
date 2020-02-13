"""Create an iteration of a DND game."""
import random
import doctest


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
    for i in range(0, syllables):
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

    return generate_consonant() + generate_vowel()


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
    if int(syllables) < 1:
        print("Error: Please make sure you're only inputting a positive integer.")
        return None
    else:
        character = {"Name": (generate_name(int(syllables)).title()),
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

        max_health = roll_hitpoints(character)
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


def roll_hitpoints(character):
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


def print_character(character):
    """
    Display the details of a character.

    :param character: A dictionary with character details.
    :precondition: The parameter character is a properly formatted dictionary
    :postcondition: The characters details will be displayed
    >>> character = {}
    >>> character["Name"] = "ji"
    >>> character["Strength"] = 5
    >>> character["Dexterity"] = 3
    >>> character["Intelligence"] = 3
    >>> character["Inventory"] = []
    >>> character["XP"] = 0
    >>> character["Class"] = "monk"
    >>> character["Race"] = "elf"
    >>> print_character(character)
    {'Name': 'ji', 'Strength': 5, 'Dexterity': 3, 'Intelligence': 3, 'Inventory': [], 'XP': 0, 'Class': 'monk', 'Race': 'elf'}
    """
    print(character)


def choose_inventory(character):
    """
    Display items in a store, then let the customer buy them.

    :param character: A properly formatted character dictionary
    :precondition: Follow the rules of the param
    :postcondition: The store will be fully operation
    """
    store_inventory = {1: "Thumbtacks of blindness", 2: "Double edged dagger", 3: "Double handled dagger",
                       4: "Longsword of bluntness", 5: "Railroads for Dummies", 6: "Ring of Detect Rings"}

    user_input = ""
    new_inventory = []
    while user_input != "-1":
        print("""
            Welcome to Cheatskape's general store!
            Here are my wares but choose wisely!
        
            1: Thumbtacks of blindness
            2: Double edged dagger
            3: Double handled dagger
            4: Longsword of bluntness
            5: Railroads for Dummies
            6: Ring of Detect Rings
            
            What would you like to buy? (-1 to finish)
            """)

        user_input = input()
        if int(user_input) == int(1) or user_input.strip().lower() == "thumbtacks of blindness":
            new_inventory.append(store_inventory[1])
        elif int(user_input) == int(2) or user_input.strip().lower() == "double edged dagger":
            new_inventory.append(store_inventory[2])
        elif int(user_input) == int(3) or user_input.strip().lower() == "double handled dagger":
            new_inventory.append(store_inventory[3])
        elif int(user_input) == int(4) or user_input.strip().lower() == "longsword of bluntness":
            new_inventory.append(store_inventory[4])
        elif int(user_input) == int(5) or user_input.strip().lower() == "railroads for Dummies":
            new_inventory.append(store_inventory[5])
        elif int(user_input) == int(6) or user_input.strip().lower() == "ring of Detect Rings":
            new_inventory.append(store_inventory[6])
        elif int(user_input) == int(-1):
            continue
        else:
            print("Please type either the name of the item, the number of the item, or -1 to leave the shop.")
    character["Inventory"] = new_inventory
    print(character)


def combat_round(opponent_one, opponent_two):
    first_turn = roll_for_initiative()
    if first_turn:  # if roll_for_initiative returns true: opponent 1 attacks first
        single_attack(opponent_one, opponent_two)  # opponent 1 attacks opponent 2
        if is_alive(opponent_two):  # if opponent 2 survived, opponent 2 retaliates
            single_attack(opponent_two, opponent_one)
    else:
        single_attack(opponent_two, opponent_one)  # if roll_for_initiative returns false: opponent 2 attacks first
        if is_alive(opponent_one):
            single_attack(opponent_one, opponent_two)


def single_attack(attacker, defender):
    """
    Complete a single attack attempt.

    :param attacker: A properly formatted character dictionary.
    :param defender: A properly formatted character dictionary.
    :precondition: Both params must be different characters that are properly formatted.
    :postcondition: A single attack will be properly completed.
    """
    attack_attempt = roll_die(1, 20)
    if attack_attempt > defender["Dexterity"]:
        damage = roll_die(1, roll_hitpoints(attacker))
        defender["HP"[1]] -= damage
        if is_alive(defender):
            print(defender["Name"] + " took the hit like a real champ but still took " + str(damage) + " damage")
        else:
            print(attacker["Name"] + " hits" + defender["Name"] + " for" + str(damage) + " damage. " + defender["Name"]
                  + " never stood a chance and now lies dead.")
    else:
        print(attacker["Name"] + " misses entirely! " + defender["Name"] + " says: Dude are you even trying?")


def is_alive(character):
    """
    Check if a character died.

    :param character: A properly formatted character dictionary.
    :precondition: The character param's rules are followed.
    :postcondition: Function will say if the character is alive or not
    :return: A boolean value representing if the character is alive.
    """
    return character["HP"[1]] > 1


def roll_for_initiative():
    """
    Roll an initiative.

    :precondition: No parameters are inputted into the function.
    :postcondition: Will decide who goes first.
    :return: A boolean value if someone goes first or not.
    """
    while True:
        roll_1 = roll_die(1, 20)
        roll_2 = roll_die(1, 20)
        if roll_1 > roll_2:
            return True
        if roll_2 > roll_1:
            return False


def main():
    print_character(create_character(input("How many syllables do you want in your name?")))
    doctest.testmod()
    print(roll_for_initiative())
    choose_inventory(create_character(input("How many syllables do you want in your name?")))


if __name__ == "__main__":
    main()
