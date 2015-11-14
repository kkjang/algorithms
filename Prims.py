import sys

def prims(mst, start, nodes):
    final_graph = dict()
    graph_vals = []
    visited = set()
    current = start
    for i in range(1, nodes + 1):
        if i == start:
            graph_vals.append([0, start])
        else:
            graph_vals.append([sys.maxint, i])
    while len(visited) < nodes:
        min_node = min((x for x in graph_vals if x[1] not in visited), key=lambda x: x[0])
        visited.add(min_node[1])
        if min_node[1] != start:
            final_graph[current] = (min_node[1], min_node[0])
            current = min_node[1]
        for adj in mst[min_node[1]]:
            if adj[0] not in final_graph:
                if adj[1] < graph_vals[adj[0]-1][0]:
                    graph_vals[adj[0]-1][0] = adj[1]            
    return final_graph


node_num, edge_num = map(int, raw_input().split())
graph = dict()
for i in range(edge_num):
    x,y,weight = map(int, raw_input().split())
    if x in graph:
        graph[x].append((y, weight))
    else:
        graph[x] = [(y, weight)]
    if y in graph:
        graph[y].append((x, weight))
    else:
        graph[y] = [(x, weight)]
start_node = input()
output_mst = prims(graph, start_node, node_num)
print sum(x[1] for x in output_mst.itervalues())
        
        