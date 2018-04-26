# Codility - L04 _ PermCheck

---
## first solution

##### Score

- task score 33
- Correctness 50
- performance 16

##### Feedback

- two elements -> [1, 1] 
- total sum is correct but not permutation
- permutation + 한 원소가 두번
- 여러개가 두번
- 한 원소가 3번
- 모두 같은 값
- 매우 큰 값 - 메모리 에러

##### code
```python
def counting(A, std_var):
    counter = [0] * (std_var+1)
    for i in range(len(A)):
        counter[A[i]] += 1
    
    return counter

def solution(A):
    # write your code in Python 3.6
    std_var = max(A) if max(A) >= len(A) else len(A)
    
    # just 1 element
    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0
    
    counter = counting(A, std_var)
    # 0 added
    if counter[0] > 0 :
        return 0
    
    # more than 1 count nums 
    else:
        if sum(counter[1:]) != std_var : 
            return 0
        else:
            return 1
    return 0
```

##### thinking..thinking..

counter 문제, length 문제

---
## second solution
#### Score
Task score 91, Correctness 100 , Performance 83
#### Feedback
MemoryError - Permutation but, very large N

#### code

Add ideal permutation's summation function 
```python
def counting(A):
    # O(N)
    counter = [0] * (max(A)+1)
    for i in range(len(A)):
        counter[A[i]] += 1
    
    return counter

def solution(A):
    # write your code in Python 3.6
    # just 1 element
    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0

    # not unique
    if len(set(A)) != len(A):
        return 0

    counter = counting(A)
    # 0 added, multiple count
    if counter[0] > 0 or len(set(counter[1:])) > 1:
        return 0
    else:
        return 1
```
---

## Third Solution 

O(N) * O(N*logN)
```python
__author__ = 'rrbb014'

def counting(A):
    # O(N)
    counter = [0] * (max(A)+1)
    for i in range(len(A)):
        counter[A[i]] += 1
    
    return counter

def ideal_perm(max_val):
    if max_val == 1:
        return 1
    if max_val % 2 == 0:
        return (max_val+1) * (max_val / 2)
    else:
        return (max_val+1) * (max_val // 2) + ((max_val+1) / 2)

def solution(A):
    # write your code in Python 3.6
    # just 1 element
    if len(A) == 1:
        if A[0] == 1:
            return 1
        else:
            return 0

    # not unique
    if len(set(A)) != len(A):
        return 0
    # total sum
    if sum(A) != ideal_perm(max(A)):
        return 0
    else:
        counter = counting(A)
        # 0 added, multiple count
        if counter[0] > 0 or len(set(counter[1:])) > 1:
            return 0
        else:
            return 1
```