def find_depends(graph):
    result = {}
    for parent, children in graph.items():
        if parent not in result:
            result[parent] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    for node, depends in result.items():
        if result[node] == 0:
            return node
    return None


graph = {}

while True:
    command = input()
    if command == 'End':
        break
    parent, child = command.split("-")
    graph[parent] = child


if find_depends(graph) is None:
    print("Acyclic: No")
else:
    print("Acyclic: Yes")

#
# def dfs(node, graph, visited, cycles):
#     if node in cycles:
#         raise Exception
#     if node in visited:
#         return
#
#     visited.add(node)
#     cycles.add(node)
#     for child in graph[node]:
#         dfs(child, graph, visited, cycles)
#     cycles.remove(node)
#
#
# graph = {}
# visited = set()
# while True:
#     command = input()
#     if command == 'End':
#         break
#     parent, child = command.split("-")
#     if parent not in graph:
#         graph[parent] = []
#     if child not in graph:
#         graph[child] = []
#     graph[parent].append(child)
#
# try:
#     for node in graph:
#         dfs(node, graph, visited, set())
#     print("Acyclic: Yes")
# except Exception:
#     print("Acyclic: No")


