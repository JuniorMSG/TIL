# 172_algorithm_theory
## 02_Dijkstra.py
"""
    참고: heapq 라이브러리 활용을 통해 우선순위 큐 사용하기
    - 데이터가 리스트 형태일 경우, 0번 인덱스를 우선순위로 인지, 우선순위가 낮은 순서대로 pop 할 수 있음
    최소 heap의 구조를 가진 코드를 쓸 수 있다.
"""
import heapq

queue = []

heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
print(queue)
for index in range(len(queue)):
    print (heapq.heappop(queue))


# 1. 그래프를 자료구조화 시킨다.
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    # 출발점과 최단거리를 보유하는 배열 생성
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # 우선순위 큐
    queue = []
    heapq.heappush(queue, [distances[start], start])
    ## 초기화 끝


    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances




print(dijkstra(mygraph, 'A'))
print(dijkstra(mygraph, 'B'))
print(dijkstra(mygraph, 'C'))