# 04_Stack.py
"""
    스택 (Stack)
    * 데이터를 제한적으로 접근할 수 있는 구조
        - 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
    * 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
        - 큐: FIFO 정책
        - 스택: LIFO 정책
"""

stack_list = list()


def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


for index in range(10):
    push(index)

print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())