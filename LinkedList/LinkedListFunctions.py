from LinkedList import LinkedList, LinkedListNode
# Write code to remove duplicates from an unsorted linked list.
def remove_duplicates(linked_list):
	current = linked_list.get_head()
	visited = {current.get_val()}
	while current.get_next() != None:
		next = current.get_next()
		next_val = next.get_val()
		if next_val in visited:
			current.set_next(next.get_next())
			continue
		else:
			visited.add(current.get_next().get_val())
		current  = current.get_next()

# Implement an algorithm to find the kth to last element of a singly linked list.
def find_kth_to_last(linked_list, k):
	length = 1
	current = linked_list.get_head()
	while current.get_next() != None:
		length += 1
		current = current.get_next()
	k_length = length - (k-1)
	iter_num = 1
	current = linked_list.get_head()
	while iter_num < k_length:
		current = current.get_next()
		iter_num += 1
	return current

# Implement an algorithm to delete a node in the middle of a singly linked list,
# given only access to that node.
def delete_middle(middle_node):
	current = middle_node
	next = current.get_next()
	current.set_val(next.get_val())
	current.set_next(next.get_next())

# Write code to partition a linked list around a value x, such that all nodes less than
# x come before all nodes greater than or equal to x.
def partition(linked_list, val):
	i = linked_list.get_head()
	j = i
	if i.get_val() < val:
		j = i.get_next()
	while i.get_next() != None:
		current = i.get_next()
		if current.get_val() < val:
			tmp_val = current.get_val()
			current.set_val(j.get_val())
			j.set_val(tmp_val)
		else:
			
		current = current.get_next()


foo = LinkedList()
bar = LinkedListNode(6)
foo.set_head(bar)
foo.add(LinkedListNode(10))
foo.add(LinkedListNode(11))
foo.add(LinkedListNode(12))
foo.add(LinkedListNode(7))
test = LinkedListNode(8)
foo.add(test)
foo.add(LinkedListNode(13))
foo.add(LinkedListNode(20))
foo.add(LinkedListNode(21))
foo.add(LinkedListNode(50))
print foo
delete_middle(test)
print foo
