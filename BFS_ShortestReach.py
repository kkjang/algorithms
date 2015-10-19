def BFS(graph_dict, root):
    if root not in graph_dict:
        return {}
    current = [root]
    visited = {root}
    levels = {root:0}
    while current:
        frontier = []
        for node in current:
            for edge in graph_dict[node]:
                if edge not in visited:
                    visited.add(edge)
                    levels[edge] = levels[node] + 1
                    frontier.append(edge)
        current = frontier
    return levels

cases = input()
for i in range(cases):
    nodes, edges = map(int, raw_input().split())
    graph = dict()
    for j in range(edges):
        x,y = map(int, raw_input().split())
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]
        if y in graph:
            graph[y].append(x)
        else:
            graph[y] = [x]
    start = input()
    shortest = BFS(graph, start)
    distance = []
    for j in range(1, nodes + 1):
        if j != start:
            if j in shortest:
                distance.append(shortest[j] * 6)
            else:
                distance.append(-1)
    print ' '.join([str(x) for x in distance])
    