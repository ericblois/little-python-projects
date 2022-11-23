import math
import itertools
import numpy as np
import random
import timeit
from typing import List

def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

def insertion_sort(numbers: List[float]):
    for i in range(1, len(numbers)):
        num = numbers[i]
        j = i - 1
        while j >= 0 and num < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = num


def eric_sort(numbers: List[float], desired_bucket_length = 10, sort_func = insertion_sort):

    # Calculate the number of buckets so that the average length of a bucket is (20)
    num_buckets = min(int(len(numbers)/desired_bucket_length), 100000) # O(1) time

    max_num = max(numbers) # O(n) time
    min_num = min(numbers) # O(n) time

    bucket_size = (max_num - min_num) / num_buckets
    buckets: List[List[float]] = [[] for _ in range(num_buckets)]
    # Put all numbers in a bucket, O(n) time
    for num in numbers:
        i = math.floor((num - min_num) / bucket_size)
        if i >= num_buckets:
            i -= 1
        buckets[i].append(num)

    last_i = 0
    # Sort buckets
    for bucket in buckets:
        #sort_func(0, len(bucket) - 1, bucket)
        sort_func(bucket)
        #bucket.sort()
        numbers[last_i : last_i + len(bucket)] = bucket
        last_i = last_i + len(bucket)

