class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None

    def __str__(self):
        return str(self.data)

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkList(object):
    def __init__(self):
        self.head = None
    
    def set_head(self, node):
        self.head = node
    
    def append(self, val):
        tmp = Node(val)
        tmp.set_next(self.head)
        self.head = tmp
        
    def get_head(self):
        return self.head
    
    def print_list(self):
        node = self.head
        while node:
            print node.data
            node = node.get_next()


def reverse_link_list(arr):
    previous = arr.get_head()
    current = previous.get_next()
    previous.set_next(None)
    while current:
    	tmp = current.get_next()
    	current.set_next(previous)
    	previous = current
    	current = tmp
    current.set_next(previous)
    arr.set_head(current)
        

bar = LinkList()
bar.append(5)
bar.append(6)
bar.append(7)
bar.append(8)
bar.append(9)
bar.append(10)
bar.print_list()
reverse_link_list(bar)
bar.print_list()