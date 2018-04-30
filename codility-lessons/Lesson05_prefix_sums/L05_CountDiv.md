# Codility -  L05 _ CountDiv

---
## 1st solution - [link](https://app.codility.com/demo/results/trainingKC6FTQ-MFP/)

O(N) 나올것이라 예상했음.

실제는 O(B-A), 리포트 받고나서 생각해보니 확실히 내가 제출한 솔루션은 입력받은 두 수의 차이에서만
<br>
계산하니 당연한 결과라 생각함. B-A란 빅오표기법을 본적은 없었지만 말이다.

### Score
- task : 50
- correctness : 100
- performance: 0

### Feedback

- big values  A=100, B=123M+, K=2
- big values2 A=101, B=123M+, K=10K
- big values3 A=0, B=Maxint, k=1~maxint
- big values4 A, B, K in 1~maxint

모두 타임아웃

### Thinking

역시나 퍼포먼스 면에서 성능이 안좋았음. 도대체 어떻게 해야 상수타임으로 나오지..

---
## next

도저히 생각이 안나 검색해보니, 이 문제는 수학문제로 보임.
<br>
솔루션 자체는 매우매우 간단하던데 여기에서 뒷받침하는 이론이 이해가 가지않았음.

---

## 2nd solution - [link](https://app.codility.com/demo/results/trainingFBF8HZ-JPR/)

며칠이 지나고 다시 풀어보면서 어느정도 솔루션의 원리를 기억은 하는데 왜 이렇게 되는지를 
<br> 
중점으로 생각하다가 갈피가 잡혀서 기록을 남긴다.
<br>
입력받는 A와 B가 무조건 B가 A보다 같거나 크다. 그리고 A와 B 둘 다 K라는 공통의 수로 "나누어진다."
<br>
여기서 나누어 진다는 개념에 좀 집중을 해보았다.
<br>
 
### 왜 범위 내의 수를 나누기로 푸는가?
나름 생각해 본것은, 나눈다라는 개념을 "영역을 쪼갠다"는 느낌으로 받아들였을때 이해가 조금 되었다.
<br>
예를 들자면, 6을 2로 나누면 3이 나오는데 이 말은 2, 4, 6 -> 3개의 영역으로 쪼갤수 있다. 는 의미고
<br>
11을 2로 나누면 5와 1/2 이지만 여기서 몫만을 생각해볼때 2의 크기로 5개의 영역으로 쪼개고 나머지 1/2만큼의 영역이 남는다.
<br>
이 문제의 제한 조건은 A와 B가 공통 범위를 공유한다는 것이다. 즉, 2의 영역으로 동일한 시작점에서 쪼개어 나가는데,
<br>
6부터 11까지 2로 나눠지는 수를 구하는 것이다. 여기서 6까지나, 11까지나 2,4,6이 공통이다. 
<br>
위에서 영역을 쪼개어 갈때 A 자신이 K로 나눠질 경우, B의 쪼개지는 서브영역들에 포함된다.
<br>
그러므로, B의 나누기 몫과 A의 나누기 몫을 빼준 값에서 A가 K로 나눠지는지에 따라 1의 증가여부가 결정된다.
<br>
수학이 또 싫어지려했던 문제였는데 이해해서 다행이다.
