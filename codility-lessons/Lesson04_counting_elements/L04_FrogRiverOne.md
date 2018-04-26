# Codility - L04 FrogRiverOne
---
## First solution 

##### Time Complexity : O(N^2)
##### Score
- Task score 63%
- Correctness 100%
- Performance 20%

##### Feedback

Performance tests

- medium_random : X = ~5000 random permutation -> TimeoutError
- large_random : X = ~10000 random permutation -> TimeoutError
- large_permutation : 
- large_large : X = 30000 arithmetic sequence -> TimeoutError

##### code

```python
def solution(X, A):
    # write your code in Python 3.6

    # unique 원소 수가 X랑 같지않으면 -1
    if len(set(A)) != X:
        return -1
    
    # 1개 존재하는데 1번일떄, 나머진 안됨
    if X == 1:
        if len(A) == 1 and A[0] == 1:
            return 0
        else:
            return -1
    
    
    # O(N)
    # 하나씩 지워나가면서 마지막 원소가 지워졌을때의 인덱스 리턴
    # 만약, 다 못지운채라면 return -1
    unique_perm = list(range(1, X+1))
    
    for idx, element in enumerate(A):
        if element in unique_perm:
            if len(unique_perm) == 1:
                return idx
            
            unique_perm.remove(element)
    
    if len(unique_perm) > 0:
        return -1
```

#### thinking..thinking..

for문 안에 list 원소가 있는지 검사하는 로직때문에 N^2이 발생하는 것으로 추정.
bit operation을 통해 실제 이상적인 수와 일치하는 순간 인덱스 리턴
ex) X = 3, 7은 이진수로 111

--- 
## Second solution

##### Time Complexity : O(N^2)
##### Score
- Task score 63 -> 72%
- Correctness 100%
- Performance 20 -> 40%

##### Feedback

Performance tests
- large_random : limit 0.58s , my time: 0.73s
- large_permutation : limit 0.58s , my time: >6.00s
- large_range : limit 0.32, my time 1.45s

##### code
```python
def solution(X, A):
    # write your code in Python 3.6

    # unique 원소 수가 X랑 같지않으면 -1
    if len(set(A)) != X:
        return -1
    
    # 1개 존재하는데 1번일떄, 나머진 안됨
    if X == 1:
        if len(A) == 1 and A[0] == 1:
            return 0
        elif list(set(A))[0] != 1:
            return -1
    
    
    # O(N)
    # 이진수로 1이 1, 2가 2, 3이 4, 4, 8
    # OR 연산으로 ideal_X 이진수 값이 동일하면 idx 반환
    unique_perm = 0
    ideal_X = int('1' * X, 2)
    
    for idx, element in enumerate(A):
        unique_perm = unique_perm | pow(2,element-1)
        if ideal_X == unique_perm:
            return idx
    
    return -1
```

##### thinking..thinking..

더이상 생각이 안나서 검색을 통해 본 결과.. counter를 이용한 비교였다. bit operation과 무슨 차이인가 싶었지만..
<br>
이미 counter에 존재하는 원소인 경우, skip이 가능한데 bit operation은 그 부분을 커버하는 것이 잘 생각나지 않았다.
<br>
하지만 counter 선언 외에, count를 체크하는 변수를 설정함으로써 counter엔 새로운 원소만 업데이트하고
<br>
새로운 원소가 딱 X만큼 들어오는 걸 점검하기 좋은 방식이란 것을 알았다.
<br>
엄밀히 내 점수는 아니지만, 솔루션 차원에서 올린다.

---
## Third solution - [link](https://app.codility.com/demo/results/trainingRVM2T9-NFZ/)

##### Time Complexity : O(N)
##### Score
- Task score 100%
- Correctness 100%
- Performance 100%
