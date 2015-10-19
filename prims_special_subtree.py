def prims(graph_dict, root):
	mstset = set()
	cur_graph = dict()
	cur_graph[root] = 0
	

nodes, edges = map(int, raw_input().split())
for i in range(edges):
    graph = dict()
    x,y,weight = map(int, raw_input().split())
    if x in graph:
        graph[x].append((y, weight))
    else:
        graph[x] = (y, weight)
    if y in graph:
        graph[y].append((x, weight))
    else:
        graph[y] = (x, weight)
start = input()
