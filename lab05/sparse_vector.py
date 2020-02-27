import doctest
"""Add and do dot-product on sparse vectors."""


def sparse_add(sparse_one: dict, sparse_two: dict):
    """
    Add two sparse vectors.

    :param sparse_one: A sparse vector in dictionary format with a 'length' key that has the true length of the dict.
    :param sparse_two: A sparse vector in dictionary format with a 'length' key that has the true length of the dict.
    :precondition: Two sparse dictionaries must be inputted as parameters and follow the rules of the params.
    :postcondition: The two dictionaries will be properly added if possible.
    :return: A dictionary of the sum of the two vectors, or None if the sum is not possible.

    >>> sparse_add({0: 1, 5: 2, 6: 1, 'length': 7}, {1: 2, 3: 2, 6: 2, 'length': 8})

    >>> sparse_add({0: 1, 5: 2, 6: 1, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8})
    {'length': 8, 0: 1, 1: 2, 3: 2, 5: 2, 6: 3}
    >>> sparse_add({4: -5, 'length': 5, 0: 4.3}, {'length': 5, 2: 7.5, 4: -6})
    {'length': 5, 0: 4.3, 2: 7.5, 4: -11}
    """
    if sparse_one['length'] == sparse_two['length']:
        new_dict = {'length': sparse_two['length']}
        counter = 0

        # adding 0's to fill the dictionaries before adding them together
        while counter < sparse_one['length']:  # sparse_one is used arbitrarily as both have the same value
            if counter not in sparse_one:
                sparse_one[counter] = 0
            if counter not in sparse_two:
                sparse_two[counter] = 0
            counter = counter + 1

        for i in range(0, len(sparse_one) - 1):  # sparse_one is used arbitrarily as both have the same value
            new_dict[i] = sparse_one[i] + sparse_two[i]
            if new_dict[i] == 0:
                new_dict.pop(i)  # remove the 0 values to shorten the sparse vector

        return new_dict
    else:
        return None


def sparse_dot_product(sparse_one: dict, sparse_two: dict):
    """
    Find the dot product of two sparse dictionaries.

    :param sparse_one: A sparse vector in dictionary format with a 'length' key that has the true length of the dict.
    :param sparse_two: A sparse vector in dictionary format with a 'length' key that has the true length of the dict.
    :precondition: Two sparse dictionaries must be inputted as parameters and follow the rules of the params.
    :postcondition: The function will find the dot product when possible.
    :return: Value of the dot product or None if the dictionaries are of different length.

    >>> sparse_dot_product({0: 1, 5: 2, 6: 1, 'length': 7}, {1: 2, 3: 2, 6: 2, 'length': 8})

    >>> sparse_dot_product({1: -2, 5: 2, 6: 5, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8})
    6
    >>> sparse_dot_product({4: -5, 'length': 5, 0: 4.3}, {'length': 5, 2: 7.5, 4: -6})
    30
    """
    if sparse_one['length'] == sparse_two['length']:
        total = 0
        for i in range(0, sparse_one['length']):
            if (i in sparse_one) and (i in sparse_two):
                total += (sparse_one[i] * sparse_two[i])
        return total

    else:
        return None


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
