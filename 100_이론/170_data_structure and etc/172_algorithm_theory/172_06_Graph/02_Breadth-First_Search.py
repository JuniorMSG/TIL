# 172_06_Graph
## 02_Breadth-First_Search.md

"""
  BFS
  - 자료구조 큐를 활용함
  - need_visit 큐와 visited 큐, 두 개의 큐를 생성
"""

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

"""

"""

def bfs(graph, start_node):
  visited = list()
  need_visit = list()

  need_visit.append(start_node)
  count = 0
  while need_visit:

    print(f'visited {visited}')
    print(f'need_visit {need_visit}')
    count += 1
    node = need_visit.pop(0)
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])

  print(f'count :: {count}')
  return visited

bfs(graph, 'A')

"""
  DFS
  - 자료구조 큐를 활용함
  - need_visit 스택과 visited 큐, 두 개의 큐를 생성
"""

print(f'=====DFS=====')
def dfs(graph, start_node):
  visited = list()
  need_visit = list()

  need_visit.append(start_node)
  count = 0
  while need_visit:

    print(f'visited {visited}')
    print(f'need_visit {need_visit}')
    count += 1
    node = need_visit.pop()
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])

  print(f'count :: {count}')
  return visited

dfs(graph, 'A')