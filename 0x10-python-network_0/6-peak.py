#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
    """ function finds the peak of elements """
    n = len(list_of_integers)
    nums = list_of_integers

    if n == 0:
        return None
    if n == 1 or nums[0] >= nums[1]:
        return nums[0]
    elif nums[n - 1] >= nums[n - 2]:
        return nums[n - 1]
    for i in range(1, n - 1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
            return nums[i]

    return None
