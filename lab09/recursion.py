import math
import time


def timer(func):
    def wrapper_timer(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        with open("results.txt", "a") as file_object:
            file_object.write(f"finished {func.__name__!r} in {run_time:.10f} secs")
        return run_time
    return wrapper_timer


def factorial_iterative(factorial):
    """
    Find the factorial.

    :param factorial: A positive integer of which factorial you need to find.
    :precondition: factorial will be a positive integer.
    :postcondition: The factorial will be properly calculated.
    :return: An integer representing the factorial

    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(3)
    6
    >>> factorial_iterative(6)
    720
    """
    total_value = 1
    if factorial == 0:
        return 1
    else:
        for value in range(1, factorial + 1):
            total_value = total_value * value
        return total_value


def factorial_recursive(factorial):
    if factorial == 0:
        return 1
    else:
        return factorial * (factorial_recursive(factorial - 1))


def main():
    print(factorial_recursive(10))


if __name__ == "__main__":
    main()