# Binary Search - book's code
import time
import random

def sequential_search(arr, X):
	N = len(arr)
	for idx in range(N):
		if arr[idx] == X:
			print('X : ', X, arr[idx])
			return idx
	print('None!')
	return None
	
def binary_search(arr, X):
	low = 0
	high = len(arr)-1
	
	while low <= high:
		mid = (low+high) // 2
		guess = arr[mid]
		if guess == X:
			
			print('X : ', X, arr[mid])
			return mid
		if guess > X:
			high = mid - 1
		if guess < X:
			low = mid + 1
	print('None!')
	return None
	
if __name__ == "__main__":

	N = random.randint(1, pow(2, 31))
	arr = range(1, N)
	X = random.randint(1, pow(2, 31))
	
	st = time.time()
	sequential_search(arr, X)
	print("binary search time: ",time.time() - st)
	
	st = time.time()
	binary_search(arr, X)
	print("binary search time: ",time.time() - st)