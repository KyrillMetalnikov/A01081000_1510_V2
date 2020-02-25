def sparse_add(sparse_one: dict, sparse_two: dict) -> dict:
    if sparse_one['length'] == sparse_two['length']:
        new_dict = {'length': len(sparse_one)}
        counter = 0
        print(len(sparse_one))

        while counter < len(sparse_one) - 1:  # sparse_one is used arbitrarily as both have the same value
            if counter not in sparse_one:
                sparse_one[counter] = 0
            if counter not in sparse_two:
                sparse_two[counter] = 0
            counter = counter + 1

        for i in range(0, len(sparse_one) - 1):  # sparse_one is used arbitrarily as both have the same value
            new_dict[i] = sparse_one[i] + sparse_two[i]

        for value in
        return new_dict


def main():
    print(sparse_add({0: 1, 5: 2, 6: 1, 'length': 8}, {1: 2, 3: 2, 6: 2, 'length': 8}))


if __name__ == "__main__":
    main()
