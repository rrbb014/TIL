# Paper summary 

## Globally Normalized Transition-based Neural Networks - [arxiv](https://arxiv.org/abs/1603.06042)

`machine-learning, natural-language-processing, POS tagging, Dependency parsing`


#### Abstract
저자는 품사 태깅, 의존성 파싱, 문장 압축 등의 task에서 SOTA 결과를 낸
<br>
**Globally Normalized Transition-based Neural Network model** 를 제안한다.
이 모델은 특정 도메인의 transition system에서 동작하는 단순한 feed-forward network이며 RNN보다 잘 동작한다고 주장한다.
<br>
local normalization 보다 global normalization의 중요성을 말하고자 하며 저자가 정의한
**label bias problem** 으로 전역적으로 normalize된 모델이 지역적으로 normalize된 모델보다 표현력이 좋은 것을 파악했다고 한다.

#### Main Question 

- What is **"locally / globally normalization"**?
- What is **"label bias problem"**?
- How can we know that the model is locally/globally normalized?
- How to implement?


1. What is **"locally / globally normalization"**?

문장 시퀀스에서 1부터 j-1 token 다음에 parser가 j에게 할 decision은 
1~j-1 상태에서 j 에 할 수 있는 모든 decision 확률의 합 중 하나 이다.

저자는 이 Z_L(d_1:j-1; \theta)를 local normalization term으로 여겼고, 
이것을 문장 전역으로 확산하기 위해 d1부터 d_j-1까지의 모든 decision 총합 
중 한 패스를 타고온 수식으로 바꾼다.

여기서 가능한 state-decision path 중 maximum값을 취할 수 있는 것이
beam search 테크닉이고 확률의 combination을 계산하기위해 softmax score를
log로 변환해서 확률의 곱들을 합으로 변환한다. 

globally normalized model의 학습은 negative log-likelihood를 loss function으로 잡고
SGD를 optimizer로 적용함.

loss function fomulation 또한, normalization term을 locally 에서 globally로 변경함.
그런데 여기서 global partition function인 Z_G (loss의 normalization term)를 계산하는게
매우 힘들다. 그걸 위해서 beam search와 early updates([Collins&Roark, 2004](http://www.aclweb.org/anthology/P04-1015))를 사용한다.

파악하기로는, 모든 State에서 모든 decision path를 계산하기 힘드니, 
beam search space 내의 것만 계산하겠다는 것으로 summation 아래 기호가 D에서 B로 바뀌었다.

2. What is **"label bias problem"** ?

locally normalized된 모델은 과거에 내린 결정사항에 대해 변경하는 것이 어렵다는 것을 label bias problem 이라고 한다.

3. How can we know that the model is locally/globally normalized?

지역적으로 현재 바라보는 word에 수행할 수 있는 decision 만을 본다면..다시말해서 소프트맥스 계산할 때 p(d_1:j-1, d_j)를 
어떤 분모로 나눠주느냐에 따라 locally/globally normalized되었다고 판단한다.

4. How to implement? 
- [링크](https://github.com/tensorflow/models/blob/master/research/syntaxnet/g3doc/syntaxnet-tutorial.md)
