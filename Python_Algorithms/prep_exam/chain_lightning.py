from queue import PriorityQueue


class Edge:
    def __init__(self, first_node, second_node, weight):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, damage, graph, damage_by_node):
    forest = {node, }
    jumps = [0] * len(graph)
    damage_by_node[node] += damage
    pq = PriorityQueue()

    [pq.put(x) for x in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = None, None

        if min_edge.first_node in forest and min_edge.second_node not in forest:
            non_tree_node = min_edge.second_node
            tree_node = min_edge.first_node
        elif min_edge.second_node in forest and min_edge.first_node not in forest:
            non_tree_node = min_edge.first_node
            tree_node = min_edge.second_node

        if non_tree_node is not None:
            forest.add(non_tree_node)
            for edge in graph[non_tree_node]:
                pq.put(edge)
            jumps[non_tree_node] = jumps[tree_node] + 1
            damage_by_node[non_tree_node] += damage // (2 ** jumps[non_tree_node])


nodes = int(input())
edges = int(input())
lights = int(input())
damage_by_node = [0] * nodes

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    first_node, second_node, weight = [int(n) for n in input().split()]
    graph[first_node].append(Edge(first_node, second_node, weight))
    graph[second_node].append(Edge(first_node, second_node, weight))
for _ in range(lights):
    node, damage = [int(s) for s in input().split()]
    prim(node, damage, graph, damage_by_node)

print(max(damage_by_node))
