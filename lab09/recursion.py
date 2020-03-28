import math
import time


def timer(func):
    def wrapper_timer(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        with open("results.txt", "a") as file_object:
            file_object.write(f"finished {func.__name__!r} in {run_time:.4f} secs")
        return run_time
    return wrapper_timer


def factorial_iterative(factorial):
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