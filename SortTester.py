import random
import time
import timeit
import numpy as np
from SortAlgos import *

random.seed(0)

LOWER_BOUND = 0
UPPER_BOUND = 100
ARRAY_SIZE = 1000000


def is_sorted(numbers: List[float]):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


# Uniform test array
TEST_ARRAY_GAUSS = [
    max(
        LOWER_BOUND,
        min(
            UPPER_BOUND,
            random.gauss(
                (UPPER_BOUND - LOWER_BOUND)/2,
                (UPPER_BOUND - LOWER_BOUND)/8
            ) + LOWER_BOUND
        )
    ) for _ in range(ARRAY_SIZE)]

TEST_ARRAY_UNIFORM = [random.uniform(LOWER_BOUND, UPPER_BOUND) for _ in range(ARRAY_SIZE)]


def test_sort_algo(sort_algo):

    test_array_gauss = TEST_ARRAY_GAUSS.copy()
    test_array_uniform = TEST_ARRAY_UNIFORM.copy()
    time_gauss = timeit.timeit(lambda: test_array_gauss.sort(), number=1)
    time_uniform = timeit.timeit(lambda: test_array_uniform.sort(), number=1)
    print("Default Python sort:\nUniform Array: " + str(round(time_uniform, 3)) + "s\nGauss Array: " + str(
        round(time_gauss, 3)) + "s\n-----")

    test_array_gauss = TEST_ARRAY_GAUSS.copy()
    test_array_uniform = TEST_ARRAY_UNIFORM.copy()
    time_gauss = timeit.timeit(lambda: np.sort(test_array_gauss), number=1)
    time_uniform = timeit.timeit(lambda: np.sort(test_array_uniform), number=1)
    print("Numpy sort:\nUniform Array: " + str(round(time_uniform, 3)) + "s\nGauss Array: " + str(
        round(time_gauss, 3)) + "s\n-----")

    test_array_gauss = TEST_ARRAY_GAUSS.copy()
    test_array_uniform = TEST_ARRAY_UNIFORM.copy()
    time_gauss = timeit.timeit(lambda: qsort(test_array_gauss), number=1)
    time_uniform = timeit.timeit(lambda: qsort(test_array_uniform), number=1)
    print("Quicksort:\nUniform Array: " + str(round(time_uniform, 3)) + "s\nGauss Array: " + str(round(time_gauss, 3)) + "s\n-----")

    test_array_gauss = TEST_ARRAY_GAUSS.copy()
    test_array_uniform = TEST_ARRAY_UNIFORM.copy()
    time_gauss = timeit.timeit(lambda: sort_algo(test_array_gauss), number=1)
    time_uniform = timeit.timeit(lambda: sort_algo(test_array_uniform), number=1)
    print("Your custom sort:\nUniform Array: " + str(round(time_uniform, 3)) + "s\nGauss Array: " + str(
        round(time_gauss, 3)) + "s\n-----")
    if is_sorted(test_array_gauss) and is_sorted(test_array_uniform):
        print("Sorting was successful")
    else:
        print("Your sorting algorithm failed to sort the array")


def main():
    test_sort_algo(eric_sort)

if __name__ == "__main__":
    main()
