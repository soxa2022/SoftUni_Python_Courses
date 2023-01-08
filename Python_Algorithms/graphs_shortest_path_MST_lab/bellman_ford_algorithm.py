from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


graph = []
nodes = int(input())
edges = int(input())

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
end = int(input())
distance = [float('inf')] * (nodes + 1)
parent = [None] * (nodes + 1)
distance[start] = 0

for _ in range(nodes - 1):
    is_update = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if distance[edge.destination] > new_distance:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            is_update = True
    if not is_update:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if distance[edge.destination] > new_distance:
        print("Negative Cycle Detected")
        break
else:
    path = deque()
    node = end
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path)
    print(distance[end])

# from collections import deque
#
#
# class Edge:
#     def __init__(self, source, destination, weight):
#         self.source = source
#         self.destination = destination
#         self.weight = weight
#
#
# graph = []
# nodes = int(input())
# edges = int(input())
#
# for _ in range(edges):
#     source, destination, weight = [int(x) for x in input().split()]
#     graph.append(Edge(source, destination, weight))
#
# start = int(input())
# end = int(input())
# distance = [float('inf')] * (nodes + 1)
# parent = [None] * (nodes + 1)
# distance[start] = 0
#
# for _ in range(nodes - 1):
#
#     for edge in graph:
#         if distance[edge.source] == float('inf'):
#             continue
#         new_distance = distance[edge.source] + edge.weight
#         if distance[edge.destination] > new_distance:
#             distance[edge.destination] = new_distance
#             parent[edge.destination] = edge.source
# is_cycle = False
# for edge in graph:
#     if distance[edge.source] == float('inf'):
#         continue
#     new_distance = distance[edge.source] + edge.weight
#     if distance[edge.destination] > new_distance:
#         is_cycle = True
#         break
# if is_cycle:
#     print("Negative Cycle Detected")
# else:
#     path = deque()
#     node = end
#     while node is not None:
#         path.appendleft(node)
#         node = parent[node]
#     print(*path)
#     print(distance[end])
