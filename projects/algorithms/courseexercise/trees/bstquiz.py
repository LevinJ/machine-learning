class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.preorder_insert(self.root, new_val)
        return
    
    def preorder_insert(self, start, new_val):
        """Helper method - use this to create a 
        recursive insert solution."""
        if new_val < start.value:
            if start.left is None:
                start.left = Node(new_val)
                return
            self.preorder_insert(start.left, new_val)
            return
        if start.right is None:
            start.right = Node(new_val)
            return
        self.preorder_insert(start.right, new_val)
        return
                
        
    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start is None:
            return False
        if start.value == find_val:
            return True
        if find_val < start.value:
            if self.preorder_search(start.left, find_val):
                return True
            else:
                return False
        if self.preorder_search(start.right, find_val):
            return True
        return False
    def search(self, find_val):
        return self.preorder_search(self.root, find_val)
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)