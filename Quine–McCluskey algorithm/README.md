# 과제: PI와 EPI 찾기

논리회로설계 20191577 김태수

## 소스코드의 내용

#### lines 1 ~ 37 (main 로직 함수인 tabular에 의해 호출되는 함수들)
- comTerm 함수: PI를 찾는 과정에서 호출되는 함수로, 이진수로 표현된 두 항들을 비교하여 한 자리만 다르다면 한 항으로 묶을 수 있으므로, 그 결과 항을 리턴하고, 아니라면 False 값을 리턴한다.
- findSet 함수: 최적화된 논리식을 찾는 과정에서 호출되는 함수로, sum of product을 구성하는 minterm 들을 모두 내포하는 sum of prime implicants 형태의 논리식을 찾아 candidates 리스트 안에 저장한다. 이 논리식들은 최적화가 되어있을수도 되어있지 않을수도 있다.
- numOperation 함수: candidates 리스트 안에 있는 논리식들을 연산의 횟수대로 정렬하여 최적화된 논리식을 찾는 과정에서 그 논리식의 연산횟수를 계산하여 리턴하는 함수
<br />
#### lines 38 ~ 165 (tabular 함수)

<br />

#### lines 43 ~ 89 (prime implicants를 찾는 과정인 step 1)

#### lines 90 ~ 108 (essential prime implicants를 찾는 과정인 step 2)

#### lines 109 ~ 165 (최적화된 논리식을 찾는 과정인 step 3)

#### lines 169 ~ (input을 받고 tabular를 호출하는 메인 함수)
