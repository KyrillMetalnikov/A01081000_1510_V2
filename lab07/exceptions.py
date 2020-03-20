"""Demonstrate proper exception protocol."""


def heron(number) -> float:
    """
    Find the square root of a number.

    A function that uses heron's theorem to find the square root of a number.
    :param number: A positive number (float or integer)
    :precondition: number must be positive.
    :postcondition: A close estimate of the square root will be found
    :return: A clsoe estimate of the square root as a float.
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


def main():
    print(heron(-5))
    print(heron(3))


if __name__ == "__main__":
    main()
