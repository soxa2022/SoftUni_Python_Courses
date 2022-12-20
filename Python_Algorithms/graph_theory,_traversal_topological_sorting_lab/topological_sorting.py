# def find_deps(graph, node: list):
#     for parent in graph:
#         for children in graph.values():
#             if parent in children:
#                 break
#         else:
#             node.append(parent)
#     return node
#
#
# nodes = int(input())
# graph = {}
# sorted_nodes = []
# for _ in range(nodes):
#     line = input().split(" ->")
#     graph[line[0]] = [] if line[1] == "" else line[1].strip().split(", ")
#
# while graph:
#     try:
#         key = find_deps(graph, [])[0]
#     except IndexError:
#         print("Invalid topological sorting")
#         break
#     sorted_nodes.append(key)
#     graph.pop(key)
#
# if sorted_nodes:
#     print(f"Topological sorting: {', '.join(sorted_nodes)}")

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

    return result


def find_node_without_depends(depends_nodes):
    for node, depends in depends_nodes.items():
        if depends_nodes[node] == 0:
            return node
    return None


nodes = int(input())
graph = {}
sorted_nodes = []
for _ in range(nodes):
    line = input().split(" ->")
    graph[line[0]] = [] if line[1] == "" else line[1].strip().split(", ")
has_cycle = False
depends_nodes = find_depends(graph)
while depends_nodes:
    node_to_remove = find_node_without_depends(depends_nodes)
    if node_to_remove is None:
        has_cycle = True
        break
    for child in graph[node_to_remove]:
        depends_nodes[child] -= 1
    depends_nodes.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)

if has_cycle:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
