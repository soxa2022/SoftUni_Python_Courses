from collections import deque


def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)
    output.appendleft(node)


graph = {}
visited = set()

while True:
    input_line = input()
    if input_line == 'End':
        break
    parent, child_str = input_line.split(' ->')
    children = [] if child_str == '' else [x for x in child_str.strip().split()]
    graph[parent] = children

output = deque()

for node in graph:
    dfs(node, graph, visited)

print(*output)
