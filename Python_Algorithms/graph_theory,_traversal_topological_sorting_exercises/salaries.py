def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if not graph[node]:
        salaries[node] = 1
        return 1
    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)
    salaries[node] = salary
    return salary


nodes = int(input())

# graph = {}
graph = []
salaries = [None] * nodes

# for row in range(nodes):
# #     line = list(input())
# #     for col in range(nodes):
# #         if "Y" not in line:
# #             graph[row] = []
# #             break
# #         if line[col] == "Y":
# #             if row not in graph:
# #                 graph[row] = [col]
# #             else:
# #                 graph[row].append(col)
for row in range(nodes):
    line = list(input())
    children = []
    for col, char in enumerate(line):
        if char == "Y":
            children.append(col)
    graph.append(children)
result = 0
for node in range(len(graph)):
    result += dfs(node, graph, salaries)

print(result)
