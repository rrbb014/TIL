# Codility - L05 _ PassingCars with python

## 1st Solution - [link](https://app.codility.com/demo/results/trainingKEV28E-8MP/)

첫 풀이에 100 찍어서 좀 흥분...처음엔 아..이걸 어떻게 O(N)으로 공간복잡도 O(1)로 하지..? 했는데,
<br>
일찍 나오는 0일 수록 자기 뒤에 나오는 1에 모두 pair가 될 수 있고, 1이 등장하면 그 뒤의 0들은 pair가 
<br>
줄어든다는걸 발견하고.. 하나씩 코딩해보고 테스트케이스 이것저것 해보며 맞춰나갔다.
<br>
그런데 코드가 안 이쁘다.. 예외사항들 집어넣고 하다보니 난잡한 느낌의 코드.
<br>
예쁜 풀이법 좀 참고해봐야겠다.

### Score

- Task score: 100
- Correctness: 100 
- Performance: 100


---
## pretty solution - [link](https://codesays.com/2014/solution-to-passing-cars-by-codility/)

내 해결책은 정방향 순회로 0, 1 카운터하고 다시 순회하는 거였는데
<br>
링크의 해결책은 역방향 순회로 루프 한번에 해결한다. 
<br>
완전 깔끔하다.
