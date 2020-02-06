import math
import doctest

"""Run the functions inside the module."""


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


def cash_money(money):
    """
    Find the lowest denomination of bills/coins possible in a value.

    :param money: A positive float up to two decimals that represents a monetary value
    :precondition: Must follow the rules of the parameter
    :postcondition: Function will find the lowest denomination
    :return: A list of integers of bills/coins used for the value

    >>> cash_money(0)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(188.93)
    [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3]
    >>> cash_money(5000)
    [50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    money = money * 100
    money_denominations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    money_divisors = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]

    while money > 0:
        for i in range(0, 11):
            money_denominations[i] = int(money / money_divisors[i])
            money %= money_divisors[i]

    return money_denominations


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
