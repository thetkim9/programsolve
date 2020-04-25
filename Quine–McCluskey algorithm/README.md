# 과제: PI와 EPI 찾기

논리회로설계 20191577 김태수

## 소스코드의 내용

#### lines 1 ~ 37 (main 로직 함수인 tabular에 의해 호출되는 함수들)
- comTerm 함수: PI를 찾는 과정에서 호출되는 함수로, 이진수로 표현된 두 항들을 비교하여 한 자리만 다르다면 한 항으로 묶을 수 있으므로, 그 결과 항을 리턴하고, 아니라면 False 값을 리턴한다.
- findSet 함수: 최적화된 논리식을 찾는 과정에서 호출되는 함수로, sum of product을 구성하는 minterm 들을 모두 내포하는 sum of prime implicants 형태의 논리식을 찾아 candidates 리스트 안에 저장한다. 이 논리식들은 최적화가 되어있을수도 되어있지 않을수도 있다.
- numOperation 함수: candidates 리스트 안에 있는 논리식들을 연산의 횟수대로 정렬하여 최적화된 논리식을 찾는 과정에서 그 논리식의 연산횟수를 계산하여 리턴하는 함수
<br />

#### lines 38 ~ 165 (tabular 함수)
quine-mccluskey 알고리즘을 구현한 코드를 담고 있는 함수로서, 메인 함수에 의해 호출을 받고, 변수들, minterm들, 그리고 don't cares를 전달받아 PI들, EPI들, 그리고 최적화된 논리식을 출력한다.
<br />

#### lines 43 ~ 89 (prime implicants를 찾는 과정인 step 1)
PI를 찾는 코드의 핵심 부분은 다음과 같다.
```python
PIs = set([])
    old = table
    new = []
    while old:
        misses = [[True for l in old[0]]]
        lenO = len(old)
        for i in range(lenO - 1):
            new.append([])
            misses.append([True for l in old[i + 1]])
            for k in range(len(old[i])):
                term = old[i][k]
                missed = True
                for j in range(len(old[i + 1])):
                    term2 = old[i + 1][j]
                    res = comTerm(term, term2, N)
                    if res:
                        new[i].append(res)
                        dict[res] = dict[term] + dict[term2]
                        misses[i + 1][j] = False
                        missed = False
                if missed and misses[i][k]:
                    PIs.add(term)
        for i in range(len(old[lenO - 1])):
            if misses[lenO - 1][i]:
                PIs.add(old[lenO - 1][i])
        old = new
        new = []
```
항들이 1의 갯수에 따라 grouping 및 나열된 후 한 그룹 내의 항들과 다른 그룹 내의 항들을 한쌍씩 비교해보며, 이 과정은 위에서 언급한 comTerm 함수를 호출함으로써 이루어진다. 결합에 한번도 포함되지 않았던 항들은 prime implicant이므로, PI라는 set에 저장된다. 더 이상 항들이 결합될 수 없을 때, old는 비게 되고, loop은 종료된다.
<br />

#### lines 90 ~ 108 (essential prime implicants를 찾는 과정인 step 2)
PI를 구한 후 EPI를 구하는 과정은 간단하다. 그냥 PI들을 구성하는 minterm들의 갯수를 다 세보고 그 갯수가 하나인 것만 찾은 다음, 그 minterm을 포함하는 PI는 EPI가 된다. 이 갯수를 찾을 때는 dictionary를 사용했다.
<br />

#### lines 109 ~ 165 (최적화된 논리식을 찾는 과정인 step 3)
이 과정은 크게 3가지 단계로 이루어져 있다. 

1번째는 논리식을 나타내는 sum of prime implicants들을 모두 찾는 것이다. 이 과정에서 앞서 언급된 findSet 함수가 호출된다.

2번째는 sum of prime implicants를 연산횟수에 따라 정렬하여, 가장 앞에 있는 것들을 찾아 res에 저장하는 것이다.

3번째는 res 안에 저장된 이 리스트 형태의 sum of prime implicants들을 처음 주어졌던 변수에 따라 논리식의 형태로 변환하는 것이다.  
<br />

#### lines 169 ~ (input을 받고 tabular를 호출하는 메인 함수)
더 이상의 자세한 설명은 생략한다.
