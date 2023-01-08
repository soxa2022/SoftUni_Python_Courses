from collections import deque


def find_path(parent, end):
    path = deque()
    if end not in parent:
        return -1
    node = parent[end]
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return len(path)


def find_shortest_path(start, end, graph):
    visited = {start, }
    parent = {start: None}

    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            break

        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            queue.append(child)
            parent[child] = node
    return parent


nodes = int(input())
count_pairs = int(input())
graph = {}

for node in range(nodes):
    node_str = input().split(':')
    parent = int(node_str[0])
    child = [] if node_str[1] == "" else [int(x) for x in node_str[1].split()]
    graph[parent] = child

for _ in range(count_pairs):
    start, end = [int(x) for x in input().split("-")]
    parent = find_shortest_path(start, end, graph)
    size = find_path(parent, end)
    print(f"{{{start}, {end}}} -> {size}")
