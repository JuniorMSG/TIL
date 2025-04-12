"""
    https://www.acmicpc.net/problem/1074
    Question    : Z
    difficulty  : 중
    Type        : 재귀

    입력
    첫째 줄에 정수 N, r, c가 주어진다.

    출력
    r행 c열을 몇 번째로 방문했는지 출력한다.

    제한
    1 ≤ N ≤ 15
    0 ≤ r, c < 2N

"""

def Q1074_test(test_case):
    array = []
    Nlst = []
    for data in test_case:
        xi, yi = data.split(" ")
        Nlst.append((xi, yi))
    print(sorted(Nlst))


def Q1074_01(n, x, y):
    # Z모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출하면 된다.
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1

        if x+1 == X and y == Y:
            print(result)
            return
        result += 1

        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return

    Q1074_01(n / 2, x, y)
    Q1074_01(n / 2, x, y+n/2)
    Q1074_01(n / 2, x+n/2, y)
    Q1074_01(n / 2, x+n/2, y+n/2)

    # 시간초과

# result = 0
# N, X, Y = map(int, input().split(" "))
# Q1074_01(2 ** N, 0, 0)


def Q1074_02(N, row, column):
    # Z모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출하면 된다.
    access_cnt = 0
    while N != 0:
        N -= 1
        # 1사분면
        if row < 2 ** N and column < 2 ** N:
            access_cnt += (2 ** N) * (2 ** N) * 0
        # 2사분면
        elif row < 2 ** N and column >= 2 ** N:
            access_cnt += (2 ** N) * (2 ** N) * 1
            column -= (2 ** N)
        # 3사분면
        elif row >= 2 ** N and column < 2 ** N:
            access_cnt += (2 ** N) * (2 ** N) * 2
            row -= (2 ** N)
        # 4사분면
        else:
            access_cnt += (2 ** N) * (2 ** N) * 3
            row -= (2 ** N)
            column -= (2 ** N)

    print(access_cnt)


# result = 0
# N, X, Y = map(int, input().split(" "))
# Q1074_02(N, X, Y)


if __name__ == '__main__':
    import sys

    sys.stdin  = open('13_Q2747.txt', 'r')
    for line in sys.stdin:
        print(line)
    temp = list(map(int, input().split(' ')))
    print(temp)


