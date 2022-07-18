# 172_05_Search
## 01_binary_search.py

def binary_search(data, search):
  print(data)
  if len(data) == 1 and search == data[0]:
    return True
  if len(data) == 1 and search != data[0]:
    return False
  if len(data) == 0:
    return False

  medium = len(data) // 2
  if search == data[medium]:
    return True
  else:
    if search > data[medium]:
      return binary_search(data[medium + 1:], search)
    else:
      return binary_search(data[:medium], search)

import random
import time
start = time.time()
data_list = random.sample(range(10000), 10000)
print(f'Time {time.time() - start}')


start = time.time()
data_list.sort()
print(f'Time {time.time() - start}')


start = time.time()
print(binary_search(data_list, 5))
print(f'Time {time.time() - start}')