import sys


class Edge:
    def __init__(self, first_node, second_node, weight):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def __str__(self):
        return f"{self.first_node} - {self.second_node}"


def find_root(parent, node):
    while not node == parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []
forest = []
max_nodes = -sys.maxsize
for _ in range(edges):
    first_node, second_node, weight = [int(n) for n in input().split(', ')]
    graph.append(Edge(first_node, second_node, weight))
    max_nodes = max(first_node, second_node, max_nodes)

parent = [x for x in range(max_nodes + 1)]

for edge in sorted(graph, key=lambda x: x.weight):
    first_root = find_root(parent, edge.first_node)
    second_root = find_root(parent, edge.second_node)
    if not first_root == second_root:
        parent[first_root] = second_root
        forest.append(edge)

[print(x) for x in forest]