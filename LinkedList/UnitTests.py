import unittest
from LinkedList import LinkedList, LinkedListNode

class TestLinkedList(unittest.TestCase):
	foo = LinkedList()
	bar = LinkedListNode(6)
	foo.set_head(bar)
	foo.add(LinkedListNode(6))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(7))
	foo.add(LinkedListNode(8))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(5))
	foo.add(LinkedListNode(5))
	def test_remove_duplicates(self):
		test = 
