# Codility Lesson 5 - Prefix sums __ GenomicRangeQuery
import random

__author__ = 'rrbb014'
T1 = ("CAGCCTA", [2, 5, 0], [4, 5, 6])
T2 = ("A", [0], [0])
T3 = ("AACCGGTTAACCGGTT", [0, 6, 10], [15, 8, 13])
T4 = ("ACGTACGT", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
T5 = ("AAAA", [0, 1, 2, 3], [3, 2, 3, 3])

# ==================== solution code
def solution(S, P, Q):
	convert_dict = {
		"A": 1,
		"C": 2,
		"G": 3,
		"T": 4,
	}
	pref = []
	res = [0] * 4
	for c in S:
		res = res.copy()
		res[convert_dict[c]-1] += 1
		pref.append(res)

	N = len(P)
	result = []
	try:
		for idx in range(N):
			res = pref[Q[idx]].copy()
			
			if P[idx] > 0:
				for idx2 in range(P[idx]):
					res[convert_dict[S[idx2]]-1] -= 1
					
			v = 1
			for i in res:
				if i == 0:
					v += 1
					continue
				else:
					result.append(v)
					break
	except(IndexError) as e:
		print('Q[idx] : %d ' % Q[idx])
		print('len(pref) : %d' % len(pref))
	return result

# =====================================

def test_solution():
	# handy test
	assert solution(*T1) == [2, 4, 1]
	assert solution(*T2) == [1]
	assert solution(*T3) == [1, 1, 2]
	assert solution(*T4) == [2, 3, 4, 1, 2]
	assert solution(*T5) == [1, 1, 1, 1]
	
	# random big case test
	for _ in range(20):
		N = random.randint(1, 10000)
		S = ''.join([random.choice(['A', 'C', 'G', 'T']) for __ in range(N)])
		K = 20000
		while K > N:
			K = random.randint(1, 5000)
		P = Q = []

		cnt = 0
		while cnt < K:
			a1 = 9999
			a2 = 0
			while a1 > a2:
				a1 = random.randint(0, N)
				a2 = random.randint(1, N)
				if a1 <= a2 and a1 < N and a2 < N:
					P.append(a1)
					Q.append(a2)
					cnt += 1
			
		if solution(S, P, Q) != simple_answer(S, P, Q):
			s1 = solution(S, P, Q)
			s2 = simple_answer(S, P, Q)
			wrong_idx = [idx for idx in range(len(s1)) if s1[idx] != s2[idx]]
			for idx in wrong_idx[:5]:
				print("idx : ", idx)
				print('P[idx] : ', P[idx])
				print('Q[idx] : ', Q[idx])
				print("S[P[idx]:Q[idx]]", S[P[idx]: Q[idx]+1])
				print('s1[idx] : ', s1[idx])
				print('s2[idx]: ', s2[idx])
				
			assert solution(S, P, Q) == simple_answer(S, P, Q)

def test_simple_answer():
	assert simple_answer(*T1) == [2, 4, 1]
	assert simple_answer(*T2) == [1]
	assert simple_answer(*T3) == [1, 1, 2]
	assert simple_answer(*T4) == [2, 3, 4, 1, 2]
	
def simple_answer(S, P, Q):
	convert = {
		"A": 1,
		"C": 2,
		"G": 3,
		"T": 4, 
	}
	
	N = len(P)
	convert_list = []
	result = []
	# 필요한 슬라이스 담아두고
	for idx in range(N):
		convert_list.append(S[P[idx] : Q[idx]+1])
	
	# 최소값을 추적해보자
	for target in convert_list:
		res = 9999
		for c in target:
			if convert[c] < res:
				res = convert[c]
		result.append(res)
	
	
	return result
	
