import math
import time


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def eratosthenes(upperbound):
    """
    Find all the prime numbers in the defined range.

    :param upperbound: An int defining the upper range of the function
    :precondition: upperbound must be a positive integer
    :postcondition: The function will return all the prime numbers less than the upperbound in a list
    :return: A list of all prime numbers between 0 and upperbound

    >>> eratosthenes(0)
    []
    >>> eratosthenes(1)
    []
    >>> eratosthenes(2)
    [2]
    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    prime_numbers = []
    for i in range(0, upperbound + 1):
        prime_numbers.append(i)
    if 0 in prime_numbers:
        prime_numbers.remove(0)
    if 1 in prime_numbers:
        prime_numbers.remove(1)
    i = 2

    while i < math.ceil(math.sqrt(upperbound)):
        if i in prime_numbers:
            for counter in range(i * 2, upperbound + 1, i):
                if counter in prime_numbers:
                    prime_numbers.remove(counter)
        i += 1

    return prime_numbers
