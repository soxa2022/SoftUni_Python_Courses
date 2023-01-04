def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


streets = []
edges = []
nodes = int(input())
count_edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(count_edges):
    first_node, second_node = [int(x) for x in input().split(" - ")]
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)
    edges.append((min(first_node, second_node), max(first_node, second_node)))

# print("Important streets:")

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)
    visited = [False] * nodes
    dfs(0, graph, visited)
    if not all(visited):
        # print(first, second)
        streets.append((first, second))
    graph[first].append(second)
    graph[second].append(first)

print("Important streets:")
for first, second in streets:
    print(first, second)
