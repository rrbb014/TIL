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
## Second solution - [link](https://app.codility.com/demo/results/trainingFUN4UF-WWF/)

결국 생각하는 시간을 너무 많이 잡아먹어서 검색을 해봄.
<br>
1차제출하고나서 이런 방식이 있을것 같은데.. 했지만 실제 구현이 머릿속에서 잘 안떠올랐던것이
<br>
https://codesays.com/2014/solution-to-max-counters-by-codility/ 여기서 확인할 수 있었다.
<br>
난 O(N)이라고 생각했던 것이 max operation때 리스트 생성을 매번 해줘야 한다는 점에서 비효율적이었던 것으로 추정된다.
<br>
사이트에선 리스트를 재생성 및 counter 초기화가 아니라 리스트 내 현재 최대값을 항상 추적하는 current_max_value와 
<br>
max operation 시, 업데이트할 값을 추적하는 max_counter를 변수로 설정.
<br>
그리고 1차 순회가 끝나고 나면 일부는 max operation이 반영되지않아있어서 이 부분을 바꿔주기위해 다시 한번 순회하면서
<br>
max_counter보다 작은 수만 max value로 업데이트 해주면 끝이다.
