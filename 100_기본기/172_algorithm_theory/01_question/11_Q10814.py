"""
    https://www.acmicpc.net/problem/10814
    Question    : 소트인사이드
    difficulty  : 하
    Type        : 정렬 / 배열

    문제
    온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

    입력
    첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

    둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

    출력
    첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

    예제 입력 1
    3
    21 Junkyu
    21 Dohyun
    20 Sunyoung

    예제 출력 1
    20 Sunyoung
    21 Junkyu
    21 Dohyun

"""

def Q10814_test(testCase):
    array = []
    for data in testCase:
        age, name = data.split(" ")
        array.append((age, name))

    print(array)
    array = sorted(array, key=lambda x: x[0])
    for data in array:
        print(data[0], data[1])


def Q10814_01():
    n = int(input())
    array = []
    for _ in range(n):
        age, name = input().split(" ")
        array.append((int(age), name))

    array = sorted(array, key=lambda x: x[0])
    for data in array:
        print(data[0], data[1])

Q10814_01()



import random
if __name__ == '__main__':
    case_01 = []
    case_01.append("21 Junkyu")
    case_01.append("21 Dohyun")
    case_01.append("20 Sunyoung")

    Q10814_test(case_01)

