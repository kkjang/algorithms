def BFS(arr, start):
	visited = [start]
	current = [start]
	while current:
		next = list()
		for i in current:
			print i
			for j in arr[i]:
				if j not in visited:
					next.append(j)
					visited.append(j)
				else:
					print "%s already visited" % j
		current = next

foo = dict()
foo['a'] = ['b', 'c']
foo['b'] = ['a','d','e']
foo['c'] = ['a', 'f']
foo['d'] = ['b']
foo['e'] = ['b','f']
foo['f'] = ['c', 'e']
BFS(foo, 'a')