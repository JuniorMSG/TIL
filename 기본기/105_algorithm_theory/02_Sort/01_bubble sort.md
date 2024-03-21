# 170_data_structure and etc
## 01_bubble sort.md

### 1. 정렬 (sorting) 이란?
- 정렬 (sorting): 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것
- 정렬은 프로그램 작성시 빈번하게 필요로 함
- 다양한 알고리즘이 고안되었으며, 알고리즘 학습의 필수

> 다양한 정렬 알고리즘 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을 이해하고,  
> 각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음


### 2. 버블 정렬 (bubble sort) 란?
* 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

#### https://visualgo.net/en/sorting

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" width=600/>

> 출처: https://en.wikipedia.org/wiki/Bubble_sort

### 3. 알고리즘 분석
    반복문이 두 개 O( 𝑛2 )
    최악의 경우,  𝑛∗(𝑛−1)2 
    완전 정렬이 되어 있는 상태라면 최선은 O(n)

```python
import random

def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
       
        if swap == False:
            break
    return data

data_list = random.sample(range(100), 50)
print(len(data_list) , data_list)
print (bubblesort(data_list))
```