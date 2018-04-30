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
	with open('2018-04-30_cache.pkl', 'wb') as f:
		fibo_cache = f.read()

def fibonacci(n):
	if n in fibo_cache.keys():
		return fibo_cache[n]
	if n <= 1:
		fibo_cache[n] = 0
		return fibo_cache[n]
	elif n == 2:
		fibo_cache[n] = 1
		return fibo_cache[n]	
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
		fibo_cache[n] = result
		return fibo_cache[n]
	

def solution(N):
	