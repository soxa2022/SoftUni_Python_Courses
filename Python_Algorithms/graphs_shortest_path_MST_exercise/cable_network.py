from queue import PriorityQueue


class Edge:
    def __init__(self, first_node, second_node, weight):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
forest = set()
for _ in range(edges):
    edge_str = input().split()
    first_node, second_node, weight = [int(s) for s in edge_str if s.isdigit()]
    edge = Edge(first_node, second_node, weight)
    graph[first_node].append(edge)
    graph[second_node].append(edge)
    if edge_str[-1] == 'connected':
        forest.add(first_node)
        forest.add(second_node)
used_budget = 0
pq = PriorityQueue()
for node in forest:
    [pq.put(x) for x in graph[node]]

while not pq.empty():
    min_edge = pq.get()
    non_forest = None
    if budget < min_edge.weight + used_budget:
        break

    if min_edge.first_node in forest and min_edge.second_node not in forest:
        non_forest = min_edge.second_node
    if min_edge.first_node not in forest and min_edge.second_node in forest:
        non_forest = min_edge.first_node
    if non_forest is not None:
        used_budget += min_edge.weight
        forest.add(non_forest)
        for edge in graph[non_forest]:
            pq.put(edge)

print(f"Budget used: {used_budget}")
