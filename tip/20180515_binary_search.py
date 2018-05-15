# 2018-05-15 STDS - binary search implementation
import random 

def binary_search(arr, X):
	high = len(arr)-1
	low = 0
	
	while low <= high:
		mid = (high+low) // 2
		if arr[mid] == X:
			return mid
		if arr[mid] > X:
			high = mid - 1
		elif arr[mid] < X:
			low = mid + 1
	
	return None
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4]
	assert binary_search(arr, 1) == 0
	assert binary_search(arr, 0) == None
	
	for _ in range(10):
		L = random.randint(1, 1000)
		arr = [random.randint(1, 10000) for __ in range(L)]
		arr.sort()
		X = random.choice(arr)

		assert binary_search(arr, X) == arr.index(X)
	