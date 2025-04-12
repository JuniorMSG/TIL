import time


def solution(S):
    # write your code in Python 3.6

    """
        문제분석 : 문자열 S 가 a/b로 이루어진 값이 주어진다.
        효율적인 알고리즘을 구할 것.
        예제케이스
        aabbb True
        ba False
        aaa True
        b True

        무슨 알고리즘을 써야 좋을까..
        조건
            N => 1 ~ 300,000
            S a andor b로 구성

        구현
        1. for문으로 구현해보자.
            1-1. b가 나오면 뒤에 a가 나오는 순간 False 리턴
            1-2. a가 나오면 뒤에 b가 나오면 BreakFlag를 셋팅하고
                 a가 다시나오면 False 리턴
    """
    flagA = False
    flagB = False
    flagBreak = False

    import time

    start = time.time()
    print(start - time.time())
    for data in S:
        if data == "a":
            flagA = True
        elif data == "b":
            flagB = True
            flagBreak = False
        if flagB and data == "a":
            return False
    print(start - time.time())

    return True
solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")