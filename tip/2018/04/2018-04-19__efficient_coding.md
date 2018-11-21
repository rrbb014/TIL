# 2018-04-19__efficient_coding

[codility](https://app.codility.com/programmers) 문제를 풀어보며

- ipython, jupyter 등 과 같은 개발환경에서 제공하는 자동완성으로 내가 얼마나 느슨한 기억에 의존해 프로그래밍 하는지 알았다.
- collections의 Counter모듈로만 counter 객체를 얻는 걸 의존했는데 그 코딩방식 중 하나를 얻었다.
- 1부터 N까지의 원소끼리 중복이 없는 순열의 합을 구할 때 for문 뿐 아니라 짝수라면, (N+1) * (N/2) 홀수라면, (N+1) * (N//2) + ((N+1)/2) 로 빠르게 구하는 법을 알았다.