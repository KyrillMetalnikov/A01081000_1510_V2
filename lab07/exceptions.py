import doctest
"""Demonstrate proper exception protocol."""


def heron(number) -> float:
    """
    Find the square root of a number.

    A function that uses heron's theorem to find the square root of a number.
    :param number: A positive number (float or integer)
    :precondition: number must be positive.
    :postcondition: A close estimate of the square root will be found
    :return: A close estimate of the square root as a float.

    >>> heron(9)
    3.0
    >>> heron(5.5)
    2.345207879911715
    """
    try:
        if number < 0:
            number / 0
    except ZeroDivisionError:
        print("Error: The number provided must be positive!")
        return -1

    square_root_guess = 1  # arbitrary value for the heron formula

    for _ in range(0, 1000):  # arbitrary amount of runs that get it close enough
        square_root_guess = (square_root_guess + (number / square_root_guess)) / 2

    return square_root_guess


def findAnEven(input_list):
    """
    Return the first even number in input_list

    :param input_list: a list of integers
    :precondition: input_list must be a list of integers
    :postcondition: return the first even number in input_list
    :raise ValueError: if input_list does not contain an even number
    :return: first even number in input_list

    >>> findAnEven([1, 3, 5, 6, 8, 9])
    6
    >>> findAnEven([2])
    2
    """
    even_number = []
    for value in input_list:
        if value % 2 == 0:
            even_number.append(value)
            break
    if len(even_number) == 0:
        raise ValueError("input_list must contain an even number!")
    return even_number[0]


def main():
    # print(heron(5.5))
    # print(heron(3))
    # print(findAnEven([1, 3, 5, 7, 9]))
    doctest.testmod()


if __name__ == "__main__":
    main()
