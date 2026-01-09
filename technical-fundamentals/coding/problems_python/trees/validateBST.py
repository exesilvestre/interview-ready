from typing import Optional
 #5. *Validate BST*
 # Implement a function to check if a binary tree is a binary search tree
class TreeNode:
    def __init__(self, value, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right


def validateBST(root):
    if not root:
        return True
    
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, min_val, max_val = stack.pop()

        if not (min_val < node.value < max_val):
            return False
        
        if node.left:
            stack.append((node.left, min_val, node.value))

        if node.right:
            stack.append((node.right, node.value, max_val))

    return True