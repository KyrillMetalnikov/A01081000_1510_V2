import math
import doctest


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
    :return: returns a list of the number of bills/coins during the denomination
    >>> cash_money(0)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> cash_money(188.93)
    [1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3]
    >>> cash_money(5000)
    [50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    money = money * 100
    money_denominations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while money > 0:
        if (money / 10000) >= 1:
            money_denominations[0] = int(money / 10000)
            money %= 10000
        if (money / 5000) >= 1:
            money_denominations[1] = int(money // 5000)
            money %= 5000
        if (money / 2000) > 1:
            money_denominations[2] = int(money // 2000)
            money %= 2000
        if (money / 1000) >= 1:
            money_denominations[3] = int(money // 1000)
            money %= 1000
        if (money / 500) >= 1:
            money_denominations[4] = int(money // 500)
            money %= 500
        if (money / 200) > 1:
            money_denominations[5] = int(money // 200)
            money %= 200
        if (money / 100) >= 1:
            money_denominations[6] = int(money // 100)
            money %= 100
        if (money / 25) >= 1:
            money_denominations[7] = int(money // 25)
            money %= 25
        if (money / 10) >= 1:
            money_denominations[8] = int(money // 10)
            money %= 10
        if (money / 5) >= 1:
            money_denominations[9] = int(money // 5)
            money %= 5
        if (money / 1) >= 1:
            money_denominations[10] = int(money // 1)
            money %= 1

    return money_denominations


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
