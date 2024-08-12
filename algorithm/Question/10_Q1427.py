"""
    https://www.acmicpc.net/problem/1427
    Question    : 소트인사이드
    difficulty  : 하
    Type        : 정렬 / 배열

    문제
    배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

    입력
    첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

    출력
    첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

    예제 입력 1
    2143
    예제 출력 1
    4321
    예제 입력 2
    999998999
    예제 출력 2
    999999998
    예제 입력 3
    61423
    예제 출력 3
    64321
    예제 입력 4
    500613009
    예제 출력 4
    965310000

"""

def Q1427_test(testCase):
    data = list(map(str, str(testCase)))
    data.sort(reverse=True)
    print("".join(data))

def Q1427_01():
    data = list(input())
    data.sort(reverse=True)
    print("".join(data))

def Q1427_02():
    array = input()
    for i in range(9, -1, -1):
        for j in array:
            if int(j) == i:
                print(i, end='')

Q1427_02()


import random
if __name__ == '__main__':
    case_01 = []
    case_01.append(2143)
    case_01.append(999998999)
    case_01.append(61423)
    case_01.append(500613009)

    for data in case_01:
        Q1427_test(data)

