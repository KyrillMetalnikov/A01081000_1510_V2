"""Demonstrate proper exception protocol."""


def heron(number: int) -> float:
    square_root_guess = 10  # arbitrary value for the heron formula
    for _ in range(0, 25):  # arbitrary amount of runs that get it close enough
        square_root_guess = (square_root_guess + (number / square_root_guess)) / 2

    return square_root_guess


def main():
    print(heron(42))


if __name__ == "__main__":
    main()
