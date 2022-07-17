# 170_data_structure and etc
## 172_03_insertion_sort.md

### 삽입 정렬 (insertion sort) 란?
* 삽입 정렬은 두 번째 인덱스부터 시작
* 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 key값이 더 작으면, B값을 뒤 인덱스로 복사
* 이를 key값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동

#### https://visualgo.net/en/sorting
<img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif" />    
  
출처: https://commons.wikimedia.org/wiki/File:Insertion-sort-example.gif


### 알고리즘 분석
    반복문이 두 개 O( 𝑛2 )
    최악의 경우,  𝑛∗(𝑛−1)2 
    완전 정렬이 되어 있는 상태라면 최선은 O(n)

```python
import random

def insertion_sort(data):

    cnt = 0
    for index in range(len(data) - 1):

        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
                cnt += 1
            else:
                break

    print(f" 스왑 횟수 {cnt}")
    return data

data_list = random.sample(range(100), 50)
print(len(data_list) , data_list)
print (insertion_sort(data_list))
```

