# Codility - L06 . MaxProductOfThree

## Trajectory

### 1st code

	[Result link](https://app.codility.com/demo/results/trainingCB4GF7-87V/)
	
	- task: 22
	- Correctness: 50
	- Performance: 0
	
	단순히 Sorting후, 마지막 인덱스 3개의 곱으로 하면 되겠지했는데, 테스트 제출 후에 좌절했음.
	<br>
	만약 [-10, -9, 0, 1, 2] 가 있으면 -부호이지만 -10과 -9를 곱하면 양수가 되버리니 제일 큰 곱의 수는
	<br>
	-10, -9, 2가 되는 것이다. 그럼 이걸 어떻게 해야할까? 
	
### 2nd code

	[Result link](https://app.codility.com/demo/results/training3S4N67-89E/)
	
	- task: 55
	- correctness: 100
	- performance: 20
	
	만약 마이너스 부호 두개에 맨 마지막 큰 수를 곱하면 제일 크지않을까 했는데 
	<br>
	correctness에선 괜찮은데 timeout error가 발생해서 performance면에서 많이 떨어졌다.
	<br>
	원인은 merge sort에 있는것같은데 그럼 이걸 어떻게 바꾸나?
	
### 3rd code

	[Result link](https://app.codility.com/demo/results/training3YJRZC-4PZ/)
	
	- task : 100
	- correctness: 100
	- performance: 20
	
	정렬하지않고 어떻게 이걸 해결하지? 라는 물음에 답이 안나와서 [여길 참고](https://codesays.com/2014/solution-to-max-product-of-three-by-codility/)했다.
	<br>
	결국 필요한 것은 가장 작은 수 2개, 가장 큰 수 3개에서 가장 작은수 2개*가장큰수1개랑 가장큰수3개를 곱한거랑 비교해서 더 큰걸 쓴다는 것이다.
	<br>
	이러면 O(N)으로 끝나고 space complexity도 O(1)로 제약조건을 만족한다.
	<br>
	진짜.. 나빼고 다 천재들 같다.
	
	
	
	