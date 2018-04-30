# Codility - L05 _ GenomicRangeQuery

---
## Problem Description

DNA구조를 "A", "C", "G", "T" 네 글자로 나타냈을 때, 각 글자의 impact factor는 
<br>
A,C,G,T 순으로 1,2,3,4 입니다. 여러 요청쿼리가 주어질 때, DNA의 특정 부분에서 가장 적은 impact factor는 몇 인지
<br>
알려주고자 합니다.

DNA시퀀스는 공백이 없는 문자열 S로 주어지며, S = S[0]S[1]...S[N-1] 로 N개의 글자가 있습니다.
<br>
비어있지 않은 배열 P와 Q에 각각 M개의 정수를 담은 M개의 쿼리가 있습니다.
<br>
K번째 인덱스 (0<= K < M) 는 P[k]에서 Q[k]사이의 DNA시퀀스에서 impact factor의 최소값을 찾고자 하는 쿼리입니다.
<br>

예를 들어...
<br>
```python
S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
```
일때, 이 M=3인 쿼리에 대한 답은 다음과 같습니다.
- P[0]=2, Q[0]=4에서 S[2]에서 S[4]까지는 'GCC'로 G는 3, C는 2의 impact factor를 가집니다. 그러므로 답은 2.
- P[1]=5, Q[1]=5에서 S[5]는 'T'이고 T=4로 답은 4.
- P[2]=0, Q[2]=6에서 S[0]에서 S[6]까지는 'CAGCCTA' 전체로 가장 작은 impact factor는 'A'로 답은 1입니다.

이러한 상황에서 다음과 같은 함수를 작성해주세요.
<br>
N개의 글자를 가진 S 문자열과 M개의 정수를 가진 두 배열 P와 Q가 주어졌을 때, 모든 쿼리에 대한 답을 구하라.
<br>
위의 예시에서 작성한 함수는 정수의 배열인 [2, 4, 1]을 리턴해야합니다.
<br>
또한 아래와 같은 조건을 가정합니다.
- 1 <= N <= 100,000
- 1 <= M <= 50,000
- P와 Q의 각 원소인 정수는 0부터 N-1의 범위를 가집니다.
- 0<= k < M일 때, P[k] <= Q[k]
- 문자열 S는 오직 영문 대문자인 'A', 'C', 'G', 'T' 만을 가집니다.
<br>

**제한조건**
<br>
시간 복잡도 : O(N+M) 
<br>
공간 복잡도 : O(N), 입력데이터는 카운팅하지 않습니다.

---
## 1st solution - [link](https://app.codility.com/demo/results/trainingMPH7HB-8AA/)

테스트 코드 작성과 솔루션코드 작성, 테스트 케이스 실험에 공을 많이 들였다.
<br>
하지만, 뭔가 large random case에서 원인파악이 안된 에러가 자꾸 발생하고
<br>
query index가 동일할 때, 많이 발생했다.

### Score
- Task score : 62
- Correctness : 80
- performance : 33

---
## 2nd solution - [link](https://app.codility.com/demo/results/training2ZEQR9-PDP/)

Correctness 100 짜리 O(N*M)의 솔루션.
<br>
로직의 변경은 없었으나, 1차에서 잘못된 부분은 mutable한 list에서의 데이터 참조 및 변경 문제로 인한 것이였다.
<br>
이후의 테스트 결과는 퍼펙트 했으나, performance 부문에선 좋지않은 해결책.

### Score
- Task score : 75
- Correctness : 100
- Performance : 33

---

## 3rd solution - [link](https://app.codility.com/demo/results/trainingD8W64Q-MZ7/)

reference - [link](https://codesays.com/2014/solution-to-genomic-range-query-by-codility/)

지금까지 갖고있던 도구로는 도저히 O(N+M)이 나올 것 같지않아 과감하게 풀이를 검색해보았다.
<br>
흥미로웠던 점은 [Segment tree](https://www.acmicpc.net/blog/view/9) 라는 것을 알게되었다는 점. (이..이런게 있었다니..!!)
<br>
구현도 따라해봤는데 손에 안 익어 연습해봐야할 듯. - [segment tree implementation](https://github.com/rrbb014/TIL/blob/master/codility-lessons/Lesson05_prefix_sums/segment_tree.py), / [reference-link](https://github.com/evgeth/segment_tree)
<br>
결론적으로 reference에 나와있는 솔루션은 인덱스 기록으로 상태기록 및 조건 검색을 O(N+M)에 해낼 수 있었다는 것.
<br>
처음엔 이해가 잘 안 가다가 천천히 보니 아주 직관적인 방식이었다. 
<br>
카운터 만들기에 정체된 내 응용부족을 알 수 있던 문제였음.
<br>
segment tree는 이 유형 외에도 여러 구간이나 slice 문제에 범용적으로 활용 할 수 있는 data structure인 듯.. 
<br>
공부해두면 유용할 것 같음.

