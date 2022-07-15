# [171]_data_structure
## [171_04]_Queue.py

"""
    링크드 리스트 (Linked List)
        * 연결 리스트라고도 함
        * 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
        * 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(self, data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)