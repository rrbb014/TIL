
"""
Codility - L05 Prefix_sums
ref: https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

최소평균값을 갖는 시작인덱스를 찾아라.
"""
__author__ = 'rrbb014'

import random


t1 = [1, 2, 3, 4, 5]
t2 = [5, 4, 3, 2, 1]
t3 = [1, 1]
t4 = [2, 2]
t5 = [1, 2]
t6 = [2, 1]
t7 = [4, 2, 2, 5, 1, 5, 8]
t8 = [703081, 477121, 548588, 881824, 676058, 611324, 966116, 610042, 323132, 30938]
t9 = [-3, -5, -8, -4, -10]

def solution(A):
	N = len(A)
	pref = A[0] + A[1]
	length = 2
	avg = pref / length
	first_index = 0
	last_index = 0
	
	for idx in range(2, N):
		if (pref + A[idx]) / (length+1) < avg:
			pref += A[idx]
			length += 1
			avg = pref / length
			if idx == N-1:
				last_index = idx
		else:
			last_index = idx-1
			break
	
	
	# 2 phase
	for idx in range(last_index):
		if length <= 2:
			break
		
		if (pref - A[idx]) / (length-1) < avg:
			pref -= A[idx]
			length -= 1
			avg = pref / length
			first_index +=1
		else:
			first_index = idx
			break
		
		
	return first_index


def simple_answer(A):
	N = len(A)
	if N == 2:
		return 0
	result = 0
	min_avg = sum(A) / N
	
	for slice_range in range(N-1, 1, -1):
		for start_idx in range(N - slice_range + 1):
			current_avg = sum(A[start_idx:start_idx+slice_range]) / slice_range
			if current_avg < min_avg:
				result = start_idx
				min_avg = min(min_avg, current_avg)
	
	return result

def test_simple_answer():
	"""Test function of simple_answer <- slow but correct solution"""
	assert simple_answer(t1) == 0
	assert simple_answer(t2) == 3
	assert simple_answer(t3) == 0
	assert simple_answer(t4) == 0
	assert simple_answer(t5) == 0
	assert simple_answer(t6) == 0
	assert simple_answer(t7) == 1
	assert simple_answer(t8) == 8
	assert simple_answer(t9) == 2

def test_solution():
	# handy case
	assert simple_answer(t1) == solution(t1)
	assert simple_answer(t2) == solution(t2)
	assert simple_answer(t3) == solution(t3)
	assert simple_answer(t4) == solution(t4)
	assert simple_answer(t5) == solution(t5)
	assert simple_answer(t6) == solution(t6)
	assert simple_answer(t7) == solution(t7)
	assert simple_answer(t8) == solution(t8)
	
	# random and big case
	for _ in range(10):
		N = random.randint(2, 100000)
		arr = [random.randint(-10000, 10000) for __ in range(N)]
		if solution(arr) != simple_answer(arr):
			print(arr)
			assert solution(arr) == simple_answer(arr)

			
if __name__ == "__main__":
	solution(t8)