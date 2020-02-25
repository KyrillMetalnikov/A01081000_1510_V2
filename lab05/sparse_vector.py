"""Add and do dot-product on sparse vectors"""


def sparse_add(sparse_one: dict, sparse_two: dict):
    """
    Add two sparse vectors.

    :param sparse_one: A sparse vector in dictionary format with a 'length' key that has the true length of the dict.
    :param sparse_two: A sparse vector in dictionary format with a 'length' key that has the true length of the dict.
    :precondition: Two sparse dictionaries must be inputted as parameters and follow the rules of the params.
    :postcondition: The two dictionaries will be properly added if possible.
    :return: A dictionary of the sum of the two vectors, or None if the sum is not possible.

    >>> sparse_add({0: 1, 5: 2, 6: 1, 'length': 7}, {1: 2, 3: 2, 6: 2, 'length': 8})
    None
    >>> sparse_add({0: 1, 5: 2, 6: 1, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8})
    {'length': 4, 0: 1, 1: 2, 3: 2, 5: 2, 6: 3}
    """
    if sparse_one['length'] == sparse_two['length']:
        new_dict = {'length': len(sparse_one)}
        counter = 0

        # adding 0's to fill the dictionaries before adding them together
        while counter < len(sparse_one) - 1:  # sparse_one is used arbitrarily as both have the same value
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


def main():
    print(sparse_add({0: 1, 5: 2, 6: 1, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8}))


if __name__ == "__main__":
    main()
