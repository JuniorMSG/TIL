"""
    https://www.acmicpc.net/problem/11650
    Question    : 좌표정렬하기
    difficulty  : 하
    Type        : 정렬 / 배열

    문제
    2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
    
    입력
    첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
    
    출력
    첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
    
    예제 입력 1 
    5
    3 4
    1 1
    1 -1
    2 2
    3 3
    예제 출력 1 
    1 -1
    1 1
    2 2
    3 3
    3 4

"""

def Q11650_test(test_case):
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


def Q11650_01():
    n = int(input())
    Nlst = []

    for i in range(n):
        xi, yi = map(int, input().split(" "))
        Nlst.append((xi, yi))
    Nlst = sorted(Nlst)

    for data in Nlst:
        print(data[0], data[1])
Q11650_01()

if __name__ == '__main__':

    case_01 = []
    case_01.append("3 4")
    case_01.append("1 1")
    case_01.append("1 -1")
    case_01.append("2 2")
    case_01.append("3 3")
    Q11650_test(case_01)


