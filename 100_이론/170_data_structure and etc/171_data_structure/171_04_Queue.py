# 171_data_structure
## [171_04]_Queue.py

import queue

"""
    Queue(): 가장 일반적인 큐 자료 구조
    LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
    PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
"""


# Default Queue
print("======== Default Queue ======")
data_queue = queue.Queue()

# put
data_queue.put("funcoding")
data_queue.put(1)
data_queue.put(999)

# size : qsize()
print(data_queue.qsize())

#
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())

print("======== LifoQueue ======")
# LifoQueue()
data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(1)
data_queue.put(999)

print(data_queue.qsize())

print(data_queue.get())
print(data_queue.get())
print(data_queue.get())

print("======== PriorityQueue ======")
# LifoQueue()
data_queue = queue.PriorityQueue()
data_queue.put((2, "funcoding"))
data_queue.put((5, 1))
data_queue.put((10, 994))

print((data_queue.qsize()))
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())


print("======== List로 Queue 만들기 ======")

queue_list = list()

## https://docs.python.org/3/tutorial/errors.html
## 파이썬에서 커스텀 에러 처리하는 방법은 없나?


class CustomError(Exception):
    pass

class ProcessCloseException(Exception):
    print("process End")

def enqueue(data):
    queue_list.append(data)


def dequeue():
    if len(queue_list) == 0:
        raise CustomError("Queue Size Zero Error")
    else:
        raise ProcessCloseException()

    data = queue_list[0]
    print(f'Dequeue :: {data}')
    del queue_list[0]
    return data

for idx in range(10):
    enqueue(idx)

print("1:::", len(queue_list))


dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
