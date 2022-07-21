# 172_algorithm_theory
## 03_DP_백준_11726.py

"""  https://www.acmicpc.net/problem/1920
    백준 1920번
    문제
    N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

    입력
    첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
    다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
    다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
    모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

    출력
    M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

    예제 입력 1
    5
    4 1 5 2 3
    5
    1 3 7 9 5
    예제 출력 1
    1
    1
    0
    0
1
"""

import random

N = int(input().strip())
N_list = list(map(int , input().strip().split(" ")))
N_list.sort()
M = int(input().strip())
M_list = list(map(int , input().strip().split(" ")))

def Q_1920(value, start, end):
    if start > end:
        return False
    median = (start + end) // 2 # 나누기에 소숫점 이하를 버리는 // 연산자(Floor Division)
    if N_list[median] > value:
        return Q_1920(value, start, median - 1)
    elif N_list[median] < value:
        return Q_1920(value, median + 1, end)
    else:
        return True

for item in M_list:
    if Q_1920(item, 0, N-1):
        print(1)
    else:
        print(0)