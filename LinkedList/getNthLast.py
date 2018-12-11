class LinkedListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __repr__(self):
    return str(self.val)

class LinkedList:
  def __init__(self, head):
    self.head = head
    self.tail = self.get_tail()
  def __str__(self):
    node_list = []
    cur_node = self.head
    while cur_node:
      node_list.append(cur_node)
      cur_node = cur_node.next
    return ",".join([str(x) for x in node_list])
  def get_tail(self):
    node = self.head
    while node:
      node = node.next
    return node
  def push(self, val):
    new_node = LinkedListNode(val)
    new_node.next = self.head
    self.head = new_node
  def pop(self):
    cur_head = self.head
    self.head = self.head.next
    return cur_head


foo = LinkedListNode(1)
bar = LinkedList(foo)
bar.push(2)
bar.push(3)
bar.push(5)

def get_nth_last(linked_list, n):
  first = linked_list.head
  second = linked_list.head
  for i in range(n):
    if second is None:
      return None
    second = second.next
  while second:
    first = first.next
    second = second.next
  return first

print(get_nth_last(bar, 5))
