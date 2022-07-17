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


def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

print(f'palindrome => {palindrome("MOMOM")}')
print(f'palindrome => {palindrome("MOSSM")}')


""" 
    문제 4. 
        1, 정수 n에 대해
        2. n이 홀수이면 3 X n + 1 을 하고,
        3. n이 짝수이면 n 을 2로 나눕니다.
        4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.
"""
def math_one(num, cnt=0):
    cnt += 1
    print(f'math_one_func {num} {cnt}')
    if num == 1:
        return num, f'실행회수 : {cnt}회'
    if num % 2 == 1:
        return math_one(3 * num + 1, cnt)
    else:
        return math_one(num / 2, cnt)

import random
num = random.randint(1, 50)
print(f' num => {num}, math_one => {math_one(num, 0)}')


""" 
    문제 5.  정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
            1+1+1+1
            1+1+2
            1+2+1
            2+1+1
            2+2
            1+3
            3+1
            정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오

    정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면
    f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴
    출처: ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Taejon 2001 
"""


def recursive_5(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    return recursive_5(data - 1) + recursive_5(data - 2) + recursive_5(data - 3)

import random
num = random.randint(1, 50)
print(f' num => {num}, recursive_5 => {recursive_5(num)}')