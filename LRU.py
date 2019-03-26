#https://leetcode.com/problems/lru-cache/submissions/

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_left(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
    
    def remove(self, node):
        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev 

class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.prev = None
        self.key = key
        self.val = val
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self.dll.remove(node)
        self.dll.append_left(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node is None:
            node = DoublyLinkedListNode(key, value)
            self.map[key] = node
            if len(self.map) > self.capacity:
                del self.map[self.dll.tail.key]
                self.dll.remove(self.dll.tail)
        else:
            node.val = value
            self.dll.remove(node)
        self.dll.append_left(node)
