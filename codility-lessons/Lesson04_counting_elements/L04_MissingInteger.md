# Codility - L04 MissingInteger

---
## First solution - [link](https://app.codility.com/demo/results/trainingFBUHFX-K48/)

O(N^2)
### Score
- Task score : 66%
- Correctness : 100%
- Performance : 25%

### Feedback
- large_1 : >6.0s , limit: 0.59
- large_2 : >6.0s , limit: 0.66
- large_3 : >6.0s , limit: 0.58

### thinking..thinking..

이미 전에 등장했었던 숫자는 skip하고 아직 미등장한 원소 중 최소값을 찾아야하니, int를 증가하는 방법으론 불가하다고 생각하여
<br>
시퀀스 정보를 담을 수 있는  list를 선언해놓자.

---
## Second solution - [link](https://app.codility.com/demo/results/trainingGXHE4Q-ARV/)

### FAIL -____-

### Score
- Task score : 22%
- Correctness : 40%
- Performance : 0%

### Feedback

중복 등장하거나 1부터 순차적으로 나오지않는 인풋에서 에러발생
테스트 케이스 부재로 인한 예외확인이 되지않았음.

### thinking..thinking..

처음 최소정수리스트를 만들때 인풋의 길이를 대상으로 만들었는데 이를 리스트의 최대값으로 생성하게 변경.
<br> 
여기서 예외사항은 음수뿐인 인풋에는 최소정수리스트를 생성못함. 그러므로 max(A)가 음수면 적당한 정수로 변경.

 
---
## Second 수정버전 - [link](https://app.codility.com/demo/results/trainingHHR2XS-2WX/)

O(N^2)
### Score

- task : 55
- correctness: 100
- performance: 0

### feedback

중/대형 데이터셋 (사이즈 =>1만) 에서 무조건 timeout이 걸림.
1차 솔루션보다 더 안좋아졌음..
아마 리스트에서 등장 후보를 하나씩 지워나가는 연산이 원인인것같음.
(1차는 int변수를 하나 설정하고 while문으로 counter리스트 순회해 미등장 최소값탐색)

---
## Third - [link](https://app.codility.com/demo/results/trainingMDNNZQ-CAJ/)

O(N) or O(N*logN)

더 이상 생각이 나지않아 검색을 했다.
<br>
카운터를 생성하고 인풋을 순회한 후, 만들어진 카운터를 다시 순회하면서 최소정수를 찾는 
<br>
어찌보면,,, 내 고민이었던 순회 중 최소정수 갱신을 그냥 카운터를 한번 더 순회한 것이다.
<br>
왜 내가 이걸 생각 못 했는지는 **시간복잡도를 잘못 파악하고 있어서**였다.
<br>
O(N)을 목표로 하기에 iteration은 무조건 한번만 해야한다는 강박에 잡혀서 생각이 거기서 고정되버렸다.
<br>
솔루션을 보고 아차..싶었던것은 iteration 후, iteration은 O(N+M)이지 O(N^2)이 아니란 것이다.
<br>
지나고보면 간단한 문제였다고 생각하지만 내가 다 부족한 탓이다.

### Score

- task: 100
- correctness: 100
- performance: 100

### Reference

- https://github.com/deanalvero/codility/blob/master/python/lesson02/MissingInteger.py
- https://codesays.com/2014/solution-to-missing-integer-by-codility/