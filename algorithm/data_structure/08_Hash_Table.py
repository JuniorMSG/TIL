# 104_data_structure
## [171_08]_Hash_Table.md

# 해쉬 테이블 (Hash Table) 간단 구현 해보기
# https://www.fun-coding.org/PL&OOP5-2.html

# 연습 1 리스트를 활용해서 해쉬 테이블 구현하기

hash_table = list([0 for i in range(8)])
print(hash_table)


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


save_data('dk', '01200123123')
save_data('da', '3333333333')

print(read_data('dc'))
print(read_data('da'))