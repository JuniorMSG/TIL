"""
    https://www.acmicpc.net/problem/2747
    Question    : 피보나치 수
    difficulty  : 하
    Type        : 재귀 함수

    문제
    피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

    이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

    n=17일때 까지 피보나치 수를 써보면 다음과 같다.

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

    n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

    입력
    첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

    출력
    첫째 줄에 n번째 피보나치 수를 출력한다.

    예제 입력 1
    10
    예제 출력 1
    55

"""

def Q2747_test(test_case):
    array = []
    # 1. 첫재 줄에 N개 입력 개수가 주어짐
    # 2. xi, yi가 주어짐
    # 3. x를 정렬하면서 y값이 증가하는 순서로 정렬

    # 4. 테스트는 3번부터
    Nlst = []
    for data in test_case:
        xi, yi = data.split(" ")
        Nlst.append((xi, yi))
    print(sorted(Nlst))


def Q2747_01(n):
    pibo = [0] * (n+1)
    pibo[0] = 0
    pibo[1] = 1
    for i in range(2, n+1):
        pibo[i] = pibo[i-1] + pibo[i-2]
    print(pibo[n])

# Q2747_01(int(input()))

def Q2747_02(n):
    # 1. 피보나치 수열의 점화식을 세운다
    # F0 = 0 F1 = 1 , Fn = Fn-1 + Fn-2
    # 2. 재귀로 구하면 2^n의 시간복잡도가 된다.
    # 3. 큰 숫자를 넣을경우 조회 자체가 안되는 현상을 볼 수 있다.
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Q2747_02(n-1) + Q2747_02(n-2)

print(Q2747_02(int(input())))

if __name__ == '__main__':

    case_01 = []
    # case_01.append("3 4")
    # case_01.append("1 1")
    # case_01.append("1 -1")
    # case_01.append("2 2")
    # case_01.append("3 3")
    # Q2747_test(case_01)


