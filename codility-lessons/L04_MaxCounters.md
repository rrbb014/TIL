# Codility - L04_MaxCounters

## First solution - [link](https://app.codility.com/demo/results/trainingMD6R6J-DB9/)

O(N*M)

대체 왜 내 솔루션이 O(N*M)인지 모르겠음.
<br>
코딜리티는 자신들이 원하는 패턴의 답을 쓰지않으면 다르게 처리하나?
<br>
어쨌든 퍼포먼스가 안좋을거라 생각은 했는데 역시나 였음.

### Score

- Task Score: 66%
- Correctness: 100%
- Performance: 40%

### Feedback

- large_random1: 2120개의 max count  operation , limit 0.51, my 1.64s
- large_random2: 10000개의 max count operation, limit 0.96 my >6s
- extreme_large: 모두 max_count operation, limit 0.99 my >6s

### thinking..thinking..

왠지 max_count operation을 실행할때 max()와 리스트생성이 시간복잡도를 잡아먹는건 아닐까 싶다.
<br>
입력을 순회만 하면서 가장 마지막의 max_operation과 index를 찾아서
<br>
index 다음부터만 카운트 해주면 나올것같았지만, 이 방법 또한 카운터 전체를 세어줘야 한다는 점에서 전혀 나은 점이 없음.
<br>
카운터를 기록하는 방식이 있을것같은데.,.


---
## Second solution - [link]()