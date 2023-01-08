from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


graph = {}
edges = int(input())

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(", ")]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))
max_nodes = max(graph.keys())
distance = [float('inf')] * (max_nodes + 1)
parent = [None] * (max_nodes + 1)
start = int(input())
end = int(input())
distance[start] = 0
pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end:
        break

    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[end] == float('inf'):
    print("There is no such path.")
else:
    print(distance[end])
    path = deque()
    node = end
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path)