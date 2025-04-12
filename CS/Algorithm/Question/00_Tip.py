from builtins import enumerate

print("=== 01. 입력 편하게 받기  ===")
user_input_data = int("5")
int_inputs_data = list(map(int, "5 4 7 1 6".split(" ")))
str_inputs_data = list(map(str, "아오 우오 이오 아옹".split(" ")))
print(f" 단일 입력 : {user_input_data}")
print(f" 복수 입력 : {int_inputs_data}")
print(f" 복수 입력 : {str_inputs_data}")


print("=== 02. Tuple 편하게 만들기 ===")
queue = list(map(int, "5 4 7 1 6".split(" ")))
queue = [(i, idx) for idx, i in enumerate(queue)]
print(queue)


print("=== 03. 최대값 뽑아오기 ===")
queue = list(map(int, "5 4 7 1 6".split(" ")))
print(f"최대값 뽑아오기 리스트 ::: => {max(queue)}")
queue = [(i, idx) for idx, i in enumerate(queue)]
print(f"최대값 뽑아오기 튜플 ::: => {max(queue, key=lambda x: x[0])[0]}")

print("=== 04. 문자열 뒤집기 ===")
string_val = "Hello World!!"
reversed_str = ""

for i in string_val:
    reversed_str = i + reversed_str

print(f"Original String: {string_val}")
print(f"기본적인 방법 : Reversed String: {reversed_str}")

print(f"파이썬스러운 방법 1 : {string_val[::-1]}")
print(f"파이썬스러운 방법 2 : {''.join(reversed(string_val))}")

## 1. 추상화
## 2. 절차적 사고
## 3. 구현
"""
    문법 에러 : 컴파일에러
    시간 초과(TLE) : 최적화 필요 
    메모리 초과 (NLE) : 최적화 필요 
    런타임 에러(RE) 과정 오류
    틀렸습니다(WA) : 수 많은 이유
        1. 제한 및 대소 관계 (이상, 이하, 초과, 미만, min, max)
        2. 예외 처리 (단, 없는 경우는 -1을 출력한다.)
        3. 입력과 출력 (공백, 양식, 순서, 정렬 유무)
        4. 시간 제한과 메모리 제한 .
        5. 알고리즘이 맞는가?
        6. 내가 생각한 로직대로 구현했나?
        7. 불필요한 반복문이 있는가?
        8. 중복은 처리했는가?
        
    ***
    1. 수치 및 조건 정리하기
    2. 전체적인 흐름 그리기
    3. 입출력 예제 이해하기 
    
    필수 알고리즘은 암기 (다다익선)
    설명과 함께 풀어보기 / 유형은 많이 풀기
    모델링을 바탕으로 기능을 가볍게 적어보기 .
    
    디버깅 연습은 필수 
    쉽고 간단한 문제를 많이 풀자
    본인만의 스타일을 만들자.
    
    연습에는 억지로 최적화 X
    꼭 정해 풀이 알기 + 풀어볼기 
    
    
    구현 : 어떤 내용이 구체적인 사실로 나타나게 함.
    
    코테에서 시뮬레이션이란?
        1. 문제상황에서 일대일 매칭
        2. 보다 효율적으로 짜는 것이 목표
        3. 최적화와 알고리즘 등 복잡한 코드로 구현
        
    Integer - 파이썬은 수의 크기 제한이 없다. / 나누기는 float가 된다. 
    => // or divmod를 사용해야한다.
    str 
    
    Short Circuit
        - or 연산에 앞 항이 참
        - and 연산에 앞 항이 거짓 
        
"""

print(chr(65))
print(ord('A'))


"""
    List Comprehension 사용하기
"""
list_arr = [i for i in range(100) if i%2==0]
print(list_arr)
import random
list_arr2 = [random.randint(1, 100) for i in range(1, 1000)]
print(list_arr2)

array_cnt = 0
A = [1, 2, 3, 4]
while array_cnt < len(A):
    if True:
        print(array_cnt)
        array_cnt += 1
        continue
    print(4)