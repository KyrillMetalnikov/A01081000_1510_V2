"""
Sort a list of colours into the order "red, white, blue".
"""
import doctest


def dijkstra(colour_list):
    """
    Sort the function by colour.

    :param colour_list: A list of strings that only contain either "red", "white", or "blue"
    :precondition: User will use correct strings in his list and not enter an empty list
    :postcondition: The list will be sorted properly
    >>> my_list = ["blue"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['blue']
    >>> my_list = ["blue", "white", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'white', 'blue']
    >>> my_list = ["red", "red", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'red', 'red']
    >>> my_list = ["red", "white", "blue"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'white', 'blue']
    >>> my_list = ["white", "white", "red", "blue", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'red', 'white', 'white', 'blue']
    >>> my_list = ["red", "blue", "red"]
    >>> dijkstra(my_list)
    >>> print(my_list)
    ['red', 'red', 'blue']
    """
    colour_list.sort(reverse=False, key=colour_sorting)


def colour_sorting(colour_list):
    """
    Return a value based on input.
    :precondition: input must be a string of either "red", "white", or "blue"
    :postcondition: The list will be sorted.

    >>> colour_sorting("red")
    1
    >>> colour_sorting("blue")
    3
    >>> colour_sorting("white")
    2
    """
    if colour_list == "red":
        return 1
    if colour_list == "white":
        return 2
    if colour_list == "blue":
        return 3


def main():
    """
    Run the functions in the module.
    """
    dutch_flag = ["red", "blue", "blue", "white", "red", "white"]
    dijkstra(dutch_flag)
    print(dutch_flag)


if __name__ == "__main__":
    main()
    doctest.testmod()
