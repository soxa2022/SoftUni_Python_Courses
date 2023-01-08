from collections import deque


def bfs(graph, start, end):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            break

        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


def reconstruct_path(parent, end):
    path = deque()
    node = end
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path


nodes = int(input())
edges = int(input())
graph = []

[graph.append([]) for _ in range(nodes + 1)]
for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start = int(input())
end = int(input())

parents = bfs(graph, start, end)
path = reconstruct_path(parents, end)
print(f"Shortest path length is: {len(path)-1}")
print(*path)