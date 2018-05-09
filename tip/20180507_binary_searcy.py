# binary search algorithm
import random 

def binary_search(arr, X):
	N = len(arr)		
	low_idx = 0
	high_idx = len(arr)-1
	mid_idx = high_idx//2 
	
	# Not exist
	if low_idx > high_idx:
		return None
	
	if N <= 2:		
		if arr[low_idx] == X:
			return True
		elif arr[high_idx] == X:
			return True
		
	# Mid value 
	if X < arr[mid_idx]:
		return binary_search(arr[low_idx:mid_idx], X)
	else:
		return binary_search(arr[mid_idx:high_idx+1], X)
	

if __name__ == "__main__":
	# N = random.randint(1, pow(2, 31)-1)
	# arr = range(1, N)
	# X = random.choice(arr)
	# binary_search(arr, X)
	arr = list(range(1, 100))
	x = random.randint(1, 200)
	print(x)
	print(x, binary_search(arr, x))