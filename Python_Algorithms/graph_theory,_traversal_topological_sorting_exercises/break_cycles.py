def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


def path(source, destination, graph):
    visited = set()
    dfs(source, graph, visited)

    return destination in visited


removed_edges = []
nodes = int(input())
graph = {}

edges = []
for _ in range(nodes):
    node, children = input().split(" -> ")
    graph[node] = children.split()
    for child in children.split():
        edges.append((node, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if source in graph[destination] and destination in graph[source]:
        graph[source].remove(destination)
        graph[destination].remove(source)
        if path(source, destination, graph):
            removed_edges.append((source, destination))
            continue
        graph[source].append(destination)
        graph[destination].append(source)
print(f"Edges to remove: {len(removed_edges)}")
for source, destination in removed_edges:
    print(f"{source} - {destination}")
