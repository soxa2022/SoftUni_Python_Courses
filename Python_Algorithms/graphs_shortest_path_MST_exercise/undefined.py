from collections import deque


def find_path(parent, node):
    result = deque()
    while node is not None:
        result.appendleft(node)
        node = parent[node]
    return result


nodes = int(input())
edges = int(input())

graph = [] * (nodes + 1)

for _ in range(edges):
    source, destination, weight = [int(s) for s in input().split()]
    graph.append((source, destination, weight))

start = int(input())
end = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes - 1):

    for edge in graph:
        source, destination, weight = edge
        if distance[source] == float('inf'):
            continue
        new_distance = distance[source] + weight
        if new_distance < distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source

for edge in graph:
    source, destination, weight = edge
    if distance[source] == float('inf'):
        continue
    new_distance = distance[source] + weight
    if new_distance < distance[destination]:
        print("Undefined")
        break
else:
    path = find_path(parent, end)
    print(*path)
    print(distance[end])
