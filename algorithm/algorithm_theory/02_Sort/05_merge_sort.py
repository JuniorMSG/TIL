# 170_data_structure and etc
## 05_merge_sort.py

import random

data_list = random.sample(range(100), 10)


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 만 남아있을 경우
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 - right 만 남아있을 경우
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)


print(mergesplit(data_list))