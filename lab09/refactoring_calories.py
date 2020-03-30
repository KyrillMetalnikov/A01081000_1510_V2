"""
refactoring_calories.py

This program initializes a dictionary, and then repeatedly prompts the user
for new food items and their associated calories. The new items are added
to the dictionary. Each time an item is added, the list of foods is printed
along with total and average calories.

The program works as is, and contains no bugs.

Unfortunately this program is just written as one big script, and is not very
well organized. It needs to use Functions like we have discussed in class, a
proper command loop, and unit tests to prove everything works.

Your tasks:

1. Refactor this program so that it is composed of short, atomic, and
   re-usable functions
2. Add a suite of unit tests that prove everything works as it should.
"""


def user_input_food_item():
    """
    Take user input.

    :precondition: Use function with no parameters.
    :postcondition: Function will take user input.
    :return: A string of the users input.
    """
    return input("Enter food item to add, or 'q' to exit: ")


def add_food_items():
    """
    Add food items with their calories based on the user input.

    :precondition: The input prompts are followed.
    :postcondition: The food items will be properly added/
    """
    _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                 "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                 "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
                 }

    # Input loop
    new_item = user_input_food_item()
    while new_item != "q":

        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        _calories[new_item] = new_item_calories

        total_calories = calculate_total_value(_calories)

        food_item_names = dict_keys_into_list(_calories)

        avg_calories = total_calories / len(_calories)

        display_food_items(food_item_names, total_calories, avg_calories)

        new_item = input("Enter food item to add, or 'q' to exit: ")


def calculate_total_value(value: dict) -> int:
    """
    Calculate the total value of the values in a dictionary.

    :param value: A dictionary with integers as the values.
    :precondition: The rules of the param must be followed.
    :postcondition: The total value will be properly calculated.
    :return: An integer representing the total value of the values in the dictionary.

    >>> calculate_total_value({"One": 1, "Two": 2, "Three": 3})
    6
    >>> calculate_total_value({})
    0
    """
    total_value = 0
    for item in value:
        total_value = total_value + value[item]
    return total_value


def display_food_items(food_item_names: list, total_calories: int, avg_calories: float):
    """
    Display all the food items and their calories.

    :param food_item_names: A list of strings representing food items.
    :param total_calories: An integer representing the total calories of all the food items.
    :param avg_calories: A float representing the average calories of the food items.
    :precondition: The rules of the params must be followed.
    :postcondition: The items and calories will be properly displayed.
    """
    print("\nFood Items:", sorted(food_item_names))
    print("Total Calories:", total_calories,
          "Average Calories: %0.1f\n" % avg_calories)


def dict_keys_into_list(dictionary: dict) -> list:
    """
    Move all the keys of a dictionary into a list.

    :param dictionary: A dictionary of key-value pairs.
    :precondition: The rules of the params must be followed.
    :postcondition: The keys of the dictionary will be moved into a list.
    :return: A list of the dictionary keys.

    >>> dict_keys_into_list({"One": 1, "Two": 2, "Three": 3})
    ["One", "Two", "Three"]
    >>> dict_keys_into_list({})
    []
    """
    item_names = []
    for item in dictionary:
        item_names.append(item)
    return item_names


def main():
    add_food_items()


if __name__ == "__main__":
    main()
