"""
Merge Sort
ref: https://www.tutorialspoint.com/python/python_sorting_algorithms.htm
"""
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    mix = merge(left, right)
    return mix

def merge(left, right):

    L_len = len(left)
    R_len = len(right)
    res = []
    while L_len > 0 and R_len > 0:
        if left[0] < right[0]:
            res.append(left[0])
            L_len -= 1
            left = left[1:]
        else:
            res.append(right[0])
            R_len -= 1
            right = right[1:]

    if L_len == 0:
        res += right
    else:
        res += left
    return res


if __name__ == "__main__":

    for _ in range(10):
        unsorted = [random.randint(1, 100) for i in range(20)]
        res_func = merge_sort(unsorted)
        benchmark = sorted(unsorted)
        assert res_func == benchmark


