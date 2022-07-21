# 172_algorithm_theory
## 01_동적 계획법, 분할 정복.md

## 동적 계획법 (Dynamic Programming)과 분할 정복 (Divide and Conquer)
"""
  문제 1.  피보나치 수열: n 을 입력받아서 계산한다.
  n 을 입력받았을 때 피보나치 수열로 결과값을 출력하세요
  피보나치 수열
  0 -> 1
  1 -> 1
  2 이상 => (n-1) + (n-2)
"""
import time
import random

# num = random.randint(1, 40)
num = 35
data_lst = random.sample(range(100), 10)

def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)

start = time.time()
print(f'fibo recursive ::: num :: {num} => {fibo(num)}')
print(f'fibo recursive ::: {time.time()-start}')

## 동적 계획법 활용
def fibo_dp(num):
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]


start = time.time()
print(f'fibo recursive ::: num :: {num} => {fibo_dp(num)}')
print(f'fibo recursive ::: {time.time() - start}')

"""
  문제 2.  
"""