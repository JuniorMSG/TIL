# data_structure
* [01. 데이터 구조란?](#1-데이터-구조란)
* [02. 대표적인 자료구조 Array](#2-배열(array))
* [03. ](#3)

### Reference  

[뒤로](README.md) / [위로](#data_structure)

## 1. 데이터 구조란?
* 자료구조, 데이터 구조, Data structure 
  * 대량의 데이터를 효율적으로 관리할 수 있는 데이터의 구조
  * 코드상에서 효율적으로 데이터를 처리하기 위해, 데이터 특성에 따라, 체계적으로 데이터를 구조화해야 함
  * 어떤 데이터 구조를 사용하느냐에 따라, 코드 효율이 달라짐

### 데이터를 어떻게 하느냐에 따라서 속도에 영향을 준다.
    어떠한 작업에 어떠한 데이터 구조를 언제, 어떻게 쓰는지 아는 것이 해당 어플리케이션의 속도에 영향을 준다.
    1. 검색
    2. 읽기 
    3. 삽입
    4. 삭제

### 효율적으로 데이터를 관리하는 예
    우편번호: 5자리 우편번호로 국가의 기초구역을 제공
    5자리 우편번호에서 앞 3자리는 시, 군, 자치구를 표기, 뒤 2자리는 일련번호로 구성

### 대표적인 자료구조
    배열, 스택, 큐, 링크드 리스트, 해쉬 테이블, 힙 등



## 2. 배열(Array)

    1. 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
    2. 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

### 배열을 사용하는 이유 
    1. 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
    2. 같은 종류의 데이터를 순차적으로 저장

#### 장점
    1. 데이터를 읽을때 빠르게 읽을 수 있다.

#### 단점
    1. 배열의 크기를 미리 선언해야한다. (파이썬은 거의 ArrayList랑 비슷해서 크게 상관없다)
    2. 검색 / 추가 / 삭제가 쉽지 않고 느리다.

#### Memory 관점에서
    READ : 인덱스로 읽으므로 매우 빠르다.
    Search : 전체를 검사해야 한다. (느리다)
    Insert : 
        Best-Case : 배열 끝에 추가할 때 
        Comm-Case : 배열 중간에 추가할 때
        Bad-Case : 배열에 앞에 추가할 때
        Worst-Case: 배열이 꽉차서 복사하고 추가할 때 
    DELETE : Insert랑 비슷함.
        Best-Case : 배열 끝에 추가할 때 
        Comm-Case : 배열 중간에 추가할 때
        Bad-Case : 배열에 앞에 추가할 때
        Worst-Case: 배열이 꽉차서 복사하고 추가할 때 


```python
data = [1,2,3,4,5]
print(data)

data = [[1, 2, 3] , [4, 5, 6], [7, 8 ,9]]
print(data)
print(data[0][0])
print(data[1][1])
# 다음 dataset에서 전체 이름 안에 M이 몇번 나왔는지 빈도수 출력

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)']
m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1
print (m_count)

```
[뒤로](README.md) / [위로](#data_structure)


