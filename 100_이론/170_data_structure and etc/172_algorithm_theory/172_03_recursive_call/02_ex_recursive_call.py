# 172_algorithm_theory
## 02_ex_recursive_call.py

""" 문제 1

"""
## 1부터 N까지 곱하시오
import random
num = random.randint(1, 50)
print(num)


def multiple(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value

print(f'일반 for문 : {multiple(num)}')

def multiple_re(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)


print(f'recursive call : {multiple_re(num)}')


"""
    문제 2. 
    숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요
"""

import random
data_lst = random.sample(range(100), 10)

##
sum = 0
print()
for data in data_lst:
    sum += data

def sum_list(num):
    if len(num) <= 1:
        return num[0]
    return num[0] + sum_list(num[1:])

print(f'data_lst1 => {data_lst} sum => {sum}')
print(f'data_lst2 => {data_lst} sum => {sum_list(data_lst)}')

""" 
    문제 3. 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
    회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
    MOTOR - ROTOM 
"""

def palindrome(n):
    print(n)
    if n == 1:
        return n

    if n % 2 == 1:
        return (palindrome((3 * n) + 1))
    else:
        return (palindrome(int(n / 2)))
