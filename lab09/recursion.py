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

