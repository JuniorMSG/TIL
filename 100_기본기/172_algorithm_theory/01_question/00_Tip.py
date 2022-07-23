

print("=== 01. 입력 편하게 받기  ===")
user_input_data = int('5')
int_inputs_data = list(map(int, '5 4 7 1 6'.split(' ')))
str_inputs_data = list(map(str, '아오 우오 이오 아옹'.split(' ')))
print(f' 단일 입력 : {user_input_data}')
print(f' 복수 입력 : {int_inputs_data}')
print(f' 복수 입력 : {str_inputs_data}')


print("=== 02. Tuple 편하게 만들기 ===")
queue = list(map(int, '5 4 7 1 6'.split(' ')))
queue = [(i, idx) for idx, i in enumerate(queue)]
print(queue)


print("=== 03. 최대값 뽑아오기 ===")
queue = list(map(int, '5 4 7 1 6'.split(' ')))
print(f'최대값 뽑아오기 리스트 ::: => {max(queue)}')
queue = [(i, idx) for idx, i in enumerate(queue)]
print(f'최대값 뽑아오기 튜플 ::: => {max(queue, key=lambda x: x[0])[0]}')

