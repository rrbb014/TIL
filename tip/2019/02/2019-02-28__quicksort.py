# quick sort
import random

def quicksort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    front = 0
    end = len(arr)-1
    mid_val = arr[mid]
    less = []
    more = []
    for idx in range(len(arr)):
        if idx == mid:
            continue
        if arr[idx] < mid_val:
            less.append(arr[idx])
        else:
            more.append(arr[idx])
    
    left = quicksort(less)
    right = quicksort(more)
    return left + [mid_val] + right

if __name__ == "__main__":
    t = [random.randint(1, 100) for _ in range(100)]
    res = quicksort(t)
    res1 = sorted(t)
    assert res == res1
    