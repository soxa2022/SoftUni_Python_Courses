from collections import deque
from queue import PriorityQueue

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for line in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = (first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start = int(input())
end = int(input())

pq = PriorityQueue()
pq.put((-100, start))

distance = [float('-inf')] * nodes
distance[start] = 100
parent = [None] * nodes

while not pq.empty():
    max_distance, node = pq.get()
    if node == end:
        break

    for source, destination, weight in graph[node]:

        child = destination if source == node else source
        new_distance = -max_distance * weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))
print(f"Most reliable path reliability: {distance[end]:.2f}%")

result = deque()
node = end
while node is not None:
    result.appendleft(node)
    node = parent[node]
print(*result, sep=' -> ')


# from collections import deque
# from queue import PriorityQueue
#
#
# class Edge:
#     def __init__(self, source, destination, weight):
#         self.source = source
#         self.destination = destination
#         self.weight = weight
#
#
# nodes = int(input())
# edges = int(input())
#
# graph = []
# [graph.append([]) for _ in range(nodes)]
#
# for line in range(edges):
#     first, second, weight = [int(x) for x in input().split()]
#     edge = Edge(first, second, weight)
#     graph[first].append(edge)
#     graph[second].append(edge)
#
# start = int(input())
# end = int(input())
#
# pq = PriorityQueue()
# pq.put((-100, start))
#
# distance = [float('-inf')] * nodes
# distance[start] = 100
# parent = [None] * nodes
#
# while not pq.empty():
#     max_distance, node = pq.get()
#     if node == end:
#         break
#
#     for edge in graph[node]:
#         child = edge.destination if edge.source == node else edge.source
#         new_distance = (-max_distance * edge.weight) / 100
#         if new_distance > distance[child]:
#             distance[child] = new_distance
#             parent[child] = node
#             pq.put((-new_distance, child))
# print(f"Most reliable path reliability: {distance[end]:.2f}%")
#
# result = deque()
# node = end
# while node is not None:
#     result.appendleft(node)
#     node = parent[node]
# print(*result, sep=' -> ')
