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

