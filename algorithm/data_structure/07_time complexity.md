# 알고리즘의 복잡도 

## 알고리즘 복잡도 계산 항목
    시간 복잡도: 알고리즘 실행 속도
    공간 복잡도: 알고리즘이 사용하는 메모리 사이즈
    가장 중요한 시간 복잡도를 꼭 이해하고 계산할 수 있어야 함

### 알고리즘 복잡도 계산이 필요한 이유
    하나의 문제를 푸는 알고리즘은 다양할 수 있음
    정수의 절대값 구하기

    1, -1 ->> 1
    방법1: 정수값을 제곱한 값에 다시 루트를 씌우기
    방법2: 정수가 음수인지 확인해서, 음수일 때만, -1을 곱하기
    다양한 알고리즘 중 어느 알고리즘이 더 좋은지를 분석하기 위해, 복잡도를 정의하고 계산함


### 알고리즘 시간 복잡도의 주요 요소
    반복문
    마찬가지로, 프로그래밍에서 시간 복잡도에 가장 영향을 많이 미치는 요소는 반복문
    입력의 크기가 커지면 커질수록 반복문이 알고리즘 수행 시간을 지배함

### 알고리즘 성능 표기법
    Big O (빅-오) 표기법: O(N)
    알고리즘 최악의 실행 시간을 표기
    가장 많이/일반적으로 사용함
    아무리 최악의 상황이라도, 이정도의 성능은 보장한다는 의미이기 때문

    Ω (오메가) 표기법: Ω(N)
    오메가 표기법은 알고리즘 최상의 실행 시간을 표기

    Θ (세타) 표기법: Θ(N)
    오메가 표기법은 알고리즘 평균 실행 시간을 표기
    시간 복잡도 계산은 반복문이 핵심 요소임을 인지하고, 계산 표기는 최상, 평균, 최악 중, 최악의 시간인 Big-O 표기법을 중심으로 익히면 됨


## 대문자 O 표기법
* 빅 오 표기법, Big-O 표기법 이라고도 부름
* O(입력)
  - 입력 n 에 따라 결정되는 시간 복잡도 함수
  - O(1), O($log n$), O(n), O(n$log n$), O($n^2$), O($2^n$), O(n!)등으로 표기함
  - 입력 n 의 크기에 따라 기하급수적으로 시간 복잡도가 늘어날 수 있음
    - O(1) < O($log n$) < O(n) < O(n$log n$) < O($n^2$) < O($2^n$) < O(n!)
      - 참고: log n 의 베이스는 2 - $log_2 n$

* 단순하게 입력 n에 따라, 몇번 실행이 되는지를 계산하면 됩니다.
  - **표현식에 가장 큰 영향을 미치는 n 의 단위로 표기합니다.**
  - n이 1이든 100이든, 1000이든, 10000이든 실행을
    - 무조건 2회(상수회) 실행한다: O(1) 
```python
    if n > 10:
         print(n)
```  
    - n에 따라, n번, n + 10 번, 또는 3n + 10 번등 실행한다: O(n)


 ```python
      variable = 1
      for num in range(3):
          for index in range(n):
               print(index)
 ```
    - n에 따라, $n^2$번, $n^2$ + 1000 번, 100$n^2$ - 100, 또는 300$n^2$ + 1번등 실행한다: O($n^2$)
 ```python
      variable = 1
      for i in range(300):
          for num in range(n):
              for index in range(n):
                   print(index)
 ```    
![img_1.png](rsc/07_time complexity_01.png) 

* 빅 오 입력값 표기 방법
  - 예: 
    - 만약 시간 복잡도 함수가 2n^2 + 3n 이라면
      - 가장 높은 차수는 2n^2  
      - 상수는 실제 큰 영향이 없음 
      - 결국 빅 오 표기법으로는 O($n^2$)