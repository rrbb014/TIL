# Codility - L09 _ MaxProfit
---

## 1st solution - [link](https://app.codility.com/demo/results/trainingTD4X6E-TPK/)

O(N^2) 나올줄 알았음..
뭔가 O(N)이 나오려면 min, max 인덱스랑 max_profit을 한번 순회하는 동안 
<br>
추적하면서 순회 종료후 갖고있는 max_profit을 리턴해주면 될것같은데
<br>
min, max가 있은 후에 min값이 나오면 이 이후 인덱스에 max값이 나올지 확신할 수 없는 상황에서 
<br>
임시 변수를 넣어줘야하나 어떻게해야하나 하다가 머릿속에서 꼬여버림..

## 2nd solution - [link](https://app.codility.com/demo/results/trainingRKQYYU-SEW/)

참고 - https://codesays.com/2014/solution-to-max-profit-by-codility/ 

쌀 때 사서 비쌀때 판다.
<br>
최대값만을 기록해놓고 max_profit이 최대인 값만을 보존하다가 return
주의점은 입력배열의 길이가 2가 안될땐 이익이 없다는 것이다.