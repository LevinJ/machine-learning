class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        self.preorder_print(self.root, traversal)
        return '-'.join(traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start is None:
            return False
        if start.value == find_val:
            return True
        if self.preorder_search(start.left, find_val):
            return True
        if self.preorder_search(start.right, find_val):
            return True
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start is None:
            return
        traversal.append(str(start.value))
        self.preorder_print(start.left, traversal)
        self.preorder_print(start.right, traversal)
        
        return traversal
    
    def breadth_first_print(self, current_queue):
        """Helper method - use this to create a 
        recursive print solution."""
        queue_lenght = len(current_queue) 
        if queue_lenght==0 :
            return
        for _ in range(queue_lenght):
            item = current_queue.pop(0)
            print item.value
            if item.left is not None:
                current_queue.append(item.left)
            if item.right is not None:
                current_queue.append(item.right)
        self.breadth_first_print(current_queue)
        return



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


tree.breadth_first_print([tree.root])

# Test search
# Should be True
print tree.search(4)
# # Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()