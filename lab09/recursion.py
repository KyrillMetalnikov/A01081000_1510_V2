import time


def timer(func):
    """
    Time a function.

    :param func: The function that is being timed.
    :precondition: Timer must be used as a wrapper function around a function.
    :postcondition: The function will be properly timed.
    :return: The amount of time the function takes to run in floating point. (seconds)
    """
    def wrapper_timer(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        with open("results.txt", "a") as file_object:
            file_object.write(f"finished {func.__name__!r} in {run_time:.10f} secs \n")
        return run_time
    return wrapper_timer


@timer
def factorial_iterative(factorial):
    """
    Find the factorial.

    Finds the factorial using a for loop.
    :param factorial: A positive integer of which factorial you need to find.
    :precondition: factorial will be a positive integer.
    :postcondition: The factorial will be properly calculated.
    :return: An integer representing the factorial
    """
    total_value = 1
    if factorial == 0:
        return 1
    else:
        for value in range(1, factorial + 1):
            total_value = total_value * value
        return total_value


@timer
def factorial_recursive(factorial):
    """
    Find the factorial.

    Finds the factorial using a recursive helper function.
    :param factorial: A positive integer of which factorial you need to find.
    :precondition: factorial will be a positive integer.
    :postcondition: The factorial will be properly calculated.
    :return: An integer representing the factorial
    """
    return factorial_recursive_helper(factorial)


def factorial_recursive_helper(factorial):
    """
    Find the factorial.

    Finds the factorial using recursion.
    :param factorial: A positive integer of which factorial you need to find.
    :precondition: factorial will be a positive integer.
    :postcondition: The factorial will be properly calculated.
    :return: An integer representing the factorial

    >>> factorial_recursive_helper(0)
    1
    >>> factorial_recursive_helper(3)
    6
    >>> factorial_recursive_helper(6)
    720
    """
    if factorial == 0:
        return 1
    else:
        return factorial * (factorial_recursive_helper(factorial - 1))


def main():
    for value in range(1, 101):
        with open("results.txt", 'a') as file_object:
            file_object.write(f"\n {value}!\n")
        factorial_iterative(value)
        factorial_recursive(value)


if __name__ == "__main__":
    main()