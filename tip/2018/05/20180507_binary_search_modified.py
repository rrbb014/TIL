# binary search algorithm
import random 

def binary_search(arr, X):		
	global low_idx
	global high_idx
	
	mid_idx = (low_idx + high_idx) // 2	
	
	if low_idx >= high_idx:
		return None
		
	# Mid value 
	if X == arr[mid_idx]:
		return mid_idx
	elif X < arr[mid_idx]:
		high_idx = mid_idx-1
		return binary_search(arr, X)
	else:
		low_idx = mid_idx + 1
		return binary_search(arr, X)
	

if __name__ == "__main__":
	for _ in range(100):
		N = random.randint(1, pow(2, 31))
		arr = range(1, N)
		X = random.randint(1, pow(2, 31))
			
		low_idx = 0
		high_idx = len(arr)-1
		
		print(X, binary_search(arr, X))