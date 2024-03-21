"""
    https://www.acmicpc.net/problem/2750
    Question    : 수 정렬하기
    difficulty  : 하
    Type        : 정렬

    문제
    N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

    입력
    첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

    출력
    첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

"""

def Q2750_01(testCase):
    testCase['case'].sort()
    print(testCase)

def Q2750():
    N = int(input())
    array = list()

    for _ in range(N):
        array.append(int(input()))

    array.sort()
    for data in array:
        print(data)

Q2750()


import random
if __name__ == '__main__':
    case_01 = []
    case_01.append({"number": 5, "case": [random.randint(1, 1000) for i in range(5)]})
    case_01.append({"number": 7, "case": [random.randint(1, 1000) for i in range(7)]})
    case_01.append({"number": 11, "case": [random.randint(1, 1000) for i in range(11)]})
    case_01.append({"number": 55, "case": [random.randint(1, 1000) for i in range(55)]})
    for data in case_01:
        Q2750_01(data)

