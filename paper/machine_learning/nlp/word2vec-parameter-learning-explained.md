# Paper Summary

## Word2Vec Parameter Learning Explained(2014) - [arxiv](https://arxiv.org/abs/1411.2738)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)

### Abstract 
(발표시기인 2014년 당시) Mikolov et al 이 2013년도에 발표한 word2vec 모델이 큰 주목을 받으면서 
<br/>
word2vec 모델 혹은 유사한 기법으로 실험하는 연구자들이 증가하는 추세지만 word2vec 모델의
<br/>
워드 임베딩 모델의 파라미터 학습 과정을 자세하고도 완벽히 설명하는 자료가 부족하다보니
<br/> 
신경망을 잘 모르는 연구자들은 이런 모델들의 동작원리를 이해하기 어렵다.
<br/>
이 논문이 기여하고자 하는 바는  word2vec 모델들과 최적화 기법의 파라미터 업데이트식을 자세하게 유도 및 설명해서
<br/>
독자들이 word embedding 모델을 직관적으로 이해하는 것이다.
<br/>
([word2vec 모델들] : CBOW, Skip-gram [최적화 기법]: negative-sampling, hierachical softmax)
<br/>
별도로, 저자는 신경망과 back-propagation의 기본적인 사항을 부록에 담았고 독자들의 직관적인 이해를 위해 
<br/>
[interactive demo](https://ronxin.github.io/wevi/) 또한 제작했다.

### Main Question

1. CBOW, Skip-gram, Negative-sampling, Hierachical softmax를 쉽게 설명하자면?


### Future Question
1. OOV 문제를 어떻게 하면 극복할 수 있을까?
2. AutoEncoder와 무엇이 다를까?