class LinkedList(object):
	def __init__(self):
		self.head = None

	def __str__(self):
		current = self.head
		values = [current.get_val()]
		while current.get_next() != None:
			values.append(current.get_next().get_val())
			current = current.get_next()
		return ', '.join([str(x) for x in values])

	def set_head(self, node):
		self.head = node

	def get_head(self):
		return self.head

	def add(self, node):
		current = self.head
		while current.get_next() != None:
			current = current.get_next()
		current.set_next(node)

class LinkedListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		return str(self.get_val())

	def get_val(self):
		return self.val

	def set_val(self, val):
		self.val = val

	def set_next(self, node):
		self.next = node

	def get_next(self):
		return self.next

