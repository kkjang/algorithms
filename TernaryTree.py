class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None
        self.end = 0
        
    def __str__(self):
        return self.val
    
    def set_left(self, node):
        self.left = node
        
    def set_middle(self, node):
        self.middle = node
        
    def set_right(self, node):
        self.right = node
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_middle(self):
        return self.middle
        
    def get_val(self):
        return self.val


def insert(root, word):
    char = word[0]
    if root is None:
        root = Node(char)
    if char > root:
        root.set_right(insert(root.get_right(), word))
    elif char < root:
        root.set_left(insert(root.get_left(), word))
    else:
        if len(word) > 1:
            root.set_middle(insert(root.get_middle(), word[1:]))
        else:
            root.end = 1
    return root


