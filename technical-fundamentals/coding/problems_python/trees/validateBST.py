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
        curr, min_val, max_val = stack.pop()
        
        if not (min_val < curr.value < max_val):
            return False
        
        if curr.left:
            stack.append((curr.left, min_val, curr.value))

        if curr.right:
            stack.append((curr.right, curr.value, max_val))
        
    return True