"""
    https://www.acmicpc.net/problem/10989
    Question    : 수 정렬하기 3
    difficulty  : 하
    Type        : 정렬

    문제
    N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
    
    입력
    첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
    
    출력
    첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
    
    예제 입력 1 
    10
    5
    2
    3
    1
    4
    2
    3
    5
    1
    7
    예제 출력 1 
    1
    1
    2
    2
    3
    3
    4
    5
    5
    7

"""

def Q10989_test(test_case):
    array = []
    # 1. 첫재 줄에 N개 입력 개수가 주어짐
    # 2. 둘째 줄부터 N개의 줄에 값을 입력함 (x<10000)
    # 3. 배열을 선언하여 데이터를 입력받는다.
    # 4. 입력 받은 데이터를 오름차순으로 정렬한다.
    # 5. n개의 줄에 출력한다.

    # Test. 테스트는 3번부터
    test_case.sort()
    for data in test_case:
        print(data)


def Q10989_01():
    # 1. 첫재 줄에 N개 입력 개수가 주어짐
    # 2. 둘째 줄부터 N개의 줄에 값을 입력함 (x<10000)
    # 3. 배열을 선언하여 데이터를 입력받는다.
    # 4. 입력 받은 데이터를 오름차순으로 정렬한다.
    # 5. n개의 줄에 출력한다.

    num = int(input())
    nums = []
    for data in range(num):
        nums.append(int(input()))
    nums.sort()

    for num in nums:
        print(num)

    ## 기본으로 하면 메모리 초과가 나온다.
Q10989_01()


def Q10989_02():
    # Idea
    # 1. 데이터 개수 최대 1000만개
    # 2. 시간 복잡도 O(N)의 정렬 알고리즘을 사용해야함.
    # 3. 수의 범위가 1 ~ 10,000이므로 계수 정렬 이용 가능
        # 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬방법
        # 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정한다.
        # 데이터가 등장한 횟수를 센다.


    # Input / OutPut
    # 1. 첫재 줄에 N개 입력 개수가 주어짐 ( 1 ~ 10,000,00 )
    # 2. 둘째 줄부터 N개의 줄에 값을 입력함 (x 1 ~ 10000)
    # ====
    # 3. N 개의 줄에 출력함

    #

    import sys
    n = int(sys.stdin.readline())
    array = [0] * 10001

    for i in range(n):
        data = int(sys.stdin.readline())
        array[data] += 1

    for i in range(10001):
        if array[i] != 0:
            for j in range(array[i]):
                print(i)
    ## 기본으로 하면 메모리 초과가 나온다.


Q10989_02()

if __name__ == '__main__':

    case_01 = []
    case_01.append("5")
    case_01.append("2")
    case_01.append("3")
    case_01.append("1")
    case_01.append("4")
    case_01.append("2")
    case_01.append("3")
    case_01.append("5")
    case_01.append("1")
    case_01.append("7")
    Q10989_test(case_01)
    Q10989_01()

