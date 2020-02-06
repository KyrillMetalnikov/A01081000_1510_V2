import doctest
"""Run statistics function."""


def statistics(stats_list):
    """
    Find the statistics of a list.

    :param stats_list: A list of only numbers
    :precondition: stats_list must be a list object that is either empty or with numbers only
    :return: returns a list of stats if list wasn't empty, else returns empty list

    >>> statistics([])
    [None, None, None, None, None]
    >>> statistics([5])
    [1, 5, 5, 5.0, 0]
    >>> statistics([1, 1, 1, 1, 1, 1, 1])
    [7, 1, 1, 1.0, 0]
    >>> statistics([0, 0, 0, 0, 0])
    [5, 0, 0, 0.0, 0]
    >>> statistics([-1, -4, 0, 25])
    [4, -4, 25, 5.0, 29]
    >>> statistics([20, 10, 5, 8, 0])
    [5, 0, 20, 8.6, 20]
    """

    if len(stats_list) != 0:
        length = len(stats_list)
        sorted_list = sorted(stats_list)  # sorting list to make finding min and max easier
        min_value = sorted_list[0]  # after sorting, smallest value will be the first element
        max_value = sorted_list[-1]  # after sorting, largest value will be the last element
        average = sum(stats_list) / length
        range_value = max_value - min_value
        return [length, min_value, max_value, average, range_value]
    else:
        return [None, None, None, None, None]


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
