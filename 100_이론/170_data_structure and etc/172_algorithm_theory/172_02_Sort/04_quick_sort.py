# 170_data_structure and etc
## 04_quick_sort.md


### 퀵 정렬 (quick sort)

def qsort(data):
    if len(data) <= 1:
        return data
    
    left, right = list(), list()
    pivot = data[0]
    
    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    
    return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100), 10)
print(qsort(data_list))


def qsort(data):
    # 위 퀵정렬 코드를 파이썬 list comprehension을 사용해서 더 깔끔하게 작성해보기
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

data_list = random.sample(range(100), 10)
print(qsort(data_list))