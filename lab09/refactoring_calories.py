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
    _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                 "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                 "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
                 }
    # Input loop
    new_item = user_input_food_item()
    while new_item != "q":

        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        _calories[new_item] = new_item_calories

        total_calories = calculate_total_calories(_calories)

        food_item_names = dict_keys_into_list(_calories)

        avg_calories = total_calories / len(_calories)

        display_food_items(food_item_names, total_calories, avg_calories)

        new_item = input("Enter food item to add, or 'q' to exit: ")


def calculate_total_calories(_calories: dict) -> int:
    total_calories = 0
    for item in _calories:
        total_calories = total_calories + _calories[item]
    return total_calories


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
    item_names = []
    for item in dictionary:
        item_names.append(item)
    return item_names


def main():
    add_food_items()


if __name__ == "__main__":
    main()
