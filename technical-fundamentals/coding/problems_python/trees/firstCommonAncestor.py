# 8. *First Common Ancestor*#
# Design an algorithm and write code to find the first common ancestor of two nodes
# in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

from typing import Optional


class TreeNode:
    def __init__(self, value, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

def firstCommonAncestor(root, p, q):
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = firstCommonAncestor(root.left, p, q)
    right = firstCommonAncestor(root.right, p, q)

    if left and right:
        return root
    
    return left or right
