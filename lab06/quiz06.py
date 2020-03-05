import math
import time


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {func.__name__!r} in {run_time:.4f} secs")
        return run_time
    return wrapper_timer


@timer
def eratosthenes(upperbound):
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


@timer
def eratosthenes_ronald(upperbound):
    numbers_list = list(range(2, upperbound + 1))
    position = 0
    if upperbound > 2:
        while numbers_list[position] < math.sqrt(upperbound):
            numbers_list = delete_multiples_of(numbers_list, numbers_list[position])
            position += 1
    return numbers_list


def delete_multiples_of(numbers_list, number):
    numbers_to_delete = []
    for i in range(len(numbers_list)):
        # For each integer in the list that is divisible by prime but is not prime, add that integer to a list
        if numbers_list[i] % number == 0 and numbers_list[i] != number:
            numbers_to_delete.append(numbers_list[i])
    for i in range(len(numbers_to_delete)):
        numbers_list.remove(numbers_to_delete[i])
    return numbers_list


@timer
def eratosthenes_ralph(upperbound):
    primes = []
    for i in range(2, upperbound + 1):
        primes.append(i)
    for i in primes:
        if i <= (math.sqrt(upperbound)):
            for j in range(i * 2, upperbound + 1, i):
                if j in primes:
                    primes.remove(j)
    return primes


def main():
    value = 1000
    kyrill = eratosthenes(value)
    ralph = eratosthenes_ralph(value)
    ronald = eratosthenes_ronald(value)
    fastest_runtime = [kyrill, ralph, ronald]
    fastest_runtime.sort()
    name = "Kyrill"
    if fastest_runtime[0] == ronald:
        name = "Ronald"
    elif fastest_runtime[0] == ralph:
        name = "Ralph"
    print(f"The fastest runtime was made by {name}")


if __name__ == "__main__":
    main()
