from queue import PriorityQueue


class Edge:
    def __init__(self, first_node, second_node, weight):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return f"{self.first_node} - {self.second_node}"


def prim(node, graph, forest, forest_edge):
    pq = PriorityQueue()
    forest.add(node)
    [pq.put(x) for x in graph[node]]

    while not pq.empty():
        min_edge = pq.get()
        no_tree_node = None

        if min_edge.first_node in forest and min_edge.second_node not in forest:
            no_tree_node = min_edge.second_node

        if min_edge.second_node in forest and min_edge.first_node not in forest:
            no_tree_node = min_edge.first_node
        if no_tree_node is not None:
            forest.add(no_tree_node)
            forest_edge.append(min_edge)
            for edge in graph[no_tree_node]:
                pq.put(edge)


edges = int(input())
graph = {}
forest = set()
forest_edges = []

for _ in range(edges):
    first_node, second_node, weight = [int(n) for n in input().split(', ')]
    if first_node not in graph:
        graph[first_node] = []
    if second_node not in graph:
        graph[second_node] = []
    graph[first_node].append(Edge(first_node, second_node, weight))
    graph[second_node].append(Edge(first_node, second_node, weight))

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

[print(x) for x in forest_edges]



# from queue import PriorityQueue
#
#
# class Edge:
#     def __init__(self, first, second, weight):
#         self.first = first
#         self.second = second
#         self.weight = weight
#
#     def __gt__(self, other):
#         return self.weight > other.weight
#
#     def __str__(self):
#         return f"{self.first} - {self.second}"
#
#
# def prim(node, graph, forest, forest_edge):
#     forest.add(node)
#     pq = PriorityQueue()
#     for edge in graph[node]:
#         pq.put(edge)
#
#     while not pq.empty():
#         min_edge = pq.get()
#         no_tree_node = -1
#
#         if min_edge.first in forest and min_edge.second not in forest:
#             no_tree_node = min_edge.second
#
#         elif min_edge.second in forest and min_edge.first not in forest:
#             no_tree_node = min_edge.first
#         if no_tree_node == -1:
#             continue
#         forest.add(no_tree_node)
#         forest_edge.append(min_edge)
#         for edge in graph[no_tree_node]:
#             pq.put(edge)
#
#
# edges = int(input())
# graph = {}
#
#
# for _ in range(edges):
#     first, second, weight = [int(n) for n in input().split(', ')]
#     if first not in graph:
#         graph[first] = []
#     if second not in graph:
#         graph[second] = []
#     edge = Edge(first, second, weight)
#     graph[first].append(edge)
#     graph[second].append(edge)
#
# forest = set()
# forest_edges = []
# for node in graph:
#     if node in forest:
#         continue
#     prim(node, graph, forest, forest_edges)
#
# [print(x) for x in forest_edges]

