# Merge Sort - Top Down Approach
# ref: wikipedia https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
import random

def TopDownMergeSort(arr):
	N = len(arr)
	if N <= 1:
		return arr
	
	left = []
	right = []
	for idx in range(N):
		if idx < N//2:
			left.append(arr[idx])
		else:
			right.append(arr[idx])
	
	left = TopDownMergeSort(left)
	right = TopDownMergeSort(right)
	
	return merge(left, right)
	
def merge(left, right):
	result = []
	
	while left != [] and right != []:
		if left[0] <= right[0]:
			result.append(left[0])
			if len(left) >= 2:
				left = left[1:]
			else:
				left.pop()
		else:
			result.append(right[0])
			if len(right) >= 2:
				right = right[1:]
			else:
				right.pop()
	while left != []:
		result.append(left[0])
		if len(left) >= 2:
			left = left[1:]
		else:
			left.pop()
	while right != []:
		result.append(right[0])
		if len(right) >= 2:
			right = right[1:]
		else:
			right.pop()
	return result
		
	

if __name__ == "__main__":
	arr = [random.randint(1, 100) for _ in range(100)]
	sorted_arr = TopDownMergeSort(arr)
	arr.sort()
	assert arr == sorted_arr
	print('sorted!')
	
