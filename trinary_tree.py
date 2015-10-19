'''
Name: Kevin Jang
Notes: Designed purposely without making any changes to the default classes and functions.
    No helper functions were used as it was assumed they were not allowed.
'''

class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""
    def __init__(self):
        self.root = None

    # NOTE: A recursive solution with helper functions would be cleaner, but not sure if allowed?
    """Inserts val into the tree. There is no need to rebalance the tree."""
    def insert(self, val):
        current = self.root
        if current is None:
            self.root = Node(val)
        else:
            while current:
                next = None
                if val > current.val:
                    next = current.right
                    if next is None:
                        current.right = Node(val)
                        return
                elif val < current.val:
                    next = current.left
                    if next is None:
                        current.left = Node(val)
                        return
                else:
                    next = current.mid
                    if next is None:
                        current.mid = Node(val)
                        return
                current = next
                
    
    # NOTE: A recursive solution with helper functions would be cleaner, but not sure if allowed?
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""
    def delete(self, val):
        current = self.root
        found = False
        parent = None
        direction = None
        # Search for a node with the value given.
        # Keep track of its parent and direction from parent.
        while current and not found:
            if val > current.val:
                parent = current
                direction = 'right'
                current = current.right
            elif val < current.val:
                parent = current
                direction = 'left'
                current = current.left
            else:
                found = True
        # Only start the modification if a node with the designated value is found.
        # This covers the corner case where the tree is empty.  
        if found:
            # If the current node has a middle child, simply update the current node with the
            # middle child's information.  Do not need to worry about further left/right children
            if current.mid:
                current.val = current.mid.val
                current.mid = current.mid.mid
            # If current node only has a left child
            elif current.left and (current.right is None):
                next = current.left
                current.val = next.val
                current.left = next.left
                current.mid = next.mid
                current.right = next.right
            # If current node only has a right child
            elif current.right and (current.left is None):
                next = current.right
                current.val = next.val
                current.left = next.left
                current.mid = next.mid
                current.right = next.right
            # If current node has both left and right child
            elif current.right and current.left:
                parent = current
                heir = parent.right
                # Run all the way down the left side of the right child.  
                # Finds the min node in the right subtree as the heir.
                while heir.left:
                    parent = heir
                    heir = heir.left
                current.val = heir.val
                current.mid = heir.mid
                # Make sure to keep any children from the heir after the swap.
                parent.left = heir.right
                
            # If current node has no child
            else:
                # Root is to be deleted and root has no children
                if val == self.root.val:
                    self.root = None
                # Root is a leaf 
                else:
                    if direction is 'left' or direction is 'right':
                        if direction is 'left':
                            parent.left = None
                        else:
                            parent.right = None