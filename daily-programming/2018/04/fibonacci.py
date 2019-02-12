"""
매일프로그래밍 - 2018.04.30 문제
피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 
정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.
예제)
Input: N = 12
Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.
"""
__author__ = 'rrbb014'

import os
import pickle

if os.path.exists('./2018-04-30_cache.pkl'):
	with open('2018-04-30_cache.pkl', 'rb') as f:
		fibo_cache = pickle.load(f)
else:
	fibo_cache = [0, 1]
	
def fibonacci(n):
	if n <= len(fibo_cache): 
		return fibo_cache[n-1]	
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
		fibo_cache.append(result)
		return fibo_cache[n-1]

def search_cumsum(fibo_keys, N):
	"""피보나치 수열 짝수의 누적합을 기록한 dictionary에서 N보다 작은 누적합 찾기"""
	
	pivot = N
	for i in range(len(fibo_keys)//2):
		target = fibo_keys[i]
		if target < N: 
			continue
		for j in range(len(fibo_keys)//2):
			compare = fibo_keys[len(fibo_keys)-1-i]
			if compare < target:
				temp = compare
				fibo_keys[len(fibo_keys)-1-i] = target
				fibo_keys[i] = temp
		
def solution(N):
	cnt = 3
	while fibo_cache[-1] < N:
		fibonacci(fibo_cnt)
		cnt += 2
	
	res_dict = {}
	cumsum = 0
	for el in fibo_cache:
		if el % 2 == 0:
			cumsum += el
		res_dict[el] = cumsum
	
	sorted_key = sorted(list(res_dict.keys()))
	n_key = -1
	idx = 0
	for k in sorted_key:
		if k > N:			
			break
		idx += 1
	print(idx)
	return res_dict[sorted_key[idx]]
	
	