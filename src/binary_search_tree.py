"""
Binary Search Tree Implementation
Following CLRS conventions with additional utility methods.

Time Complexity:
    - insert: O(log n) average, O(n) worst
    - search: O(log n) average, O(n) worst  
    - delete: O(log n) average, O(n) worst
    
Space Complexity: O(n) for tree storage
"""

class TreeNode:
    """Node in a binary search tree."""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # For easier deletion
    
    def __repr__(self):
        return f"TreeNode({self.value})"


class BST:
    """
    Binary Search Tree with standard operations.
    
    Attributes:
        root (TreeNode): Root node of the tree
        size (int): Number of nodes in the tree
    """
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, value):
        """
        Insert a value into the BST.
        
        Args:
            value: The value to insert (must be comparable)
            
        Returns:
            bool: True if inserted, False if duplicate
        """
        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
            return True
        
        return self._insert_helper(self.root, value)
    
    def _insert_helper(self, node, value):
        """Recursive helper for insertion."""
        if value == node.value:
            return False  # Duplicates not allowed
        
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                node.left.parent = node
                self.size += 1
                return True
            return self._insert_helper(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                node.right.parent = node
                self.size += 1
                return True
            return self._insert_helper(node.right, value)
    
    def search(self, value):
        """
        Search for a value in the BST.
        
        Args:
            value: The value to search for
            
        Returns:
            bool: True if found, False otherwise
        """
        return self._search_helper(self.root, value)
    
    def _search_helper(self, node, value):
        """Recursive helper for search."""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)
    
    def delete(self, value):
        """
        Delete a value from the BST.
        
        Args:
            value: The value to delete
            
        Returns:
            bool: True if deleted, False if not found
        """
        node_to_delete = self._find_node(self.root, value)
        if node_to_delete is None:
            return False
        
        self._delete_node(node_to_delete)
        self.size -= 1
        return True
    
    def _find_node(self, node, value):
        """Find and return the node with given value."""
        if node is None:
            return None
        
        if value == node.value:
            return node
        elif value < node.value:
            return self._find_node(node.left, value)
        else:
            return self._find_node(node.right, value)
    
    def _delete_node(self, node):
        """Delete a specific node from the tree."""
        # Case 1: Node has no children (leaf)
        if node.left is None and node.right is None:
            self._replace_node(node, None)
        
        # Case 2: Node has only right child
        elif node.left is None:
            self._replace_node(node, node.right)
        
        # Case 3: Node has only left child
        elif node.right is None:
            self._replace_node(node, node.left)
        
        # Case 4: Node has both children
        else:
            # Find inorder successor (minimum in right subtree)
            successor = self._find_min(node.right)
            node.value = successor.value
            self._delete_node(successor)
    
    def _replace_node(self, node, replacement):
        """Replace node with replacement in the tree."""
        if node.parent is None:
            self.root = replacement
        elif node == node.parent.left:
            node.parent.left = replacement
        else:
            node.parent.right = replacement
        
        if replacement is not None:
            replacement.parent = node.parent
    
    def _find_min(self, node):
        """Find the minimum value node in a subtree."""
        while node.left is not None:
            node = node.left
        return node
    
    def inorder(self):
        """
        Get all values in sorted order.
        
        Returns:
            list: Sorted list of all values in the tree
        """
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        """Recursive helper for inorder traversal."""
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
    
    def height(self):
        """
        Calculate the height of the tree.
        
        Returns:
            int: Height of the tree (0 for empty tree)
        """
        return self._height_helper(self.root)
    
    def _height_helper(self, node):
        """Recursive helper for height calculation."""
        if node is None:
            return 0
        return 1 + max(self._height_helper(node.left), 
                       self._height_helper(node.right))
    
    def is_valid(self):
        """
        Verify if the tree satisfies BST property.
        
        Returns:
            bool: True if valid BST, False otherwise
        """
        return self._is_valid_helper(self.root, float('-inf'), float('inf'))
    
    def _is_valid_helper(self, node, min_val, max_val):
        """Recursive helper for BST validation."""
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_valid_helper(node.left, min_val, node.value) and
                self._is_valid_helper(node.right, node.value, max_val))
    
    def __len__(self):
        return self.size
    
    def __bool__(self):
        return self.root is not None
    
    def __str__(self):
        if not self.root:
            return "Empty BST"
        return f"BST(root={self.root.value}, size={self.size})"
