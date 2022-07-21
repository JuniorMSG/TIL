# 173_coding_test
## 173_01_BinaryGap.py

"""
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
    For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

    Write a function:

    def solution(N)
        that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
        For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
        Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..2,147,483,647].
"""

"""
    영문을 요약하면 바이너리간 0, 1간의 개수를 세는 문제
    N은 integer within the range [1..2,147,483,647] 라고 표현됨.
    
    1.0, "111" 이런 숫자형의 다른 타입이 들어올 수 있다고 생각하여 
    type이 int가 아닐때 한번 처리하자 .
    
    
"""


def number_type_check(N):
    _inputNum = N
    if type(_inputNum) is int:
        _inputNum = int(_inputNum)
    else:
        try:
            _inputNum = int(_inputNum)
        except:
            raise Exception("Not Number form")
    return _inputNum


def binary_gap(N):
    # write your code in Python 3.6
    try:
        _inputNum = number_type_check(N)
        _binary = bin(_inputNum)[2:]
        _binaryLst = _binary.strip('0').strip('1').split('1')
        _binaryGapLen = len(max(_binaryLst))
        return _binaryGapLen
    except Exception as e:
        _message = e.args[0]
        return _message


print(binary_gap("STR"))