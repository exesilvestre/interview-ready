# 4. *Check Balanced*#
#
#  Implement a function
#  to check if a binary tree is balanced.
#
#  For the purposes of this question, a balanced tree is defined to be a tree
#
#  such that the heights of the two subtrees of any node never differ by more than one.


from typing import Optional


class TreeNode:
    def __init__(self, value, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

    
def checkBalanced( tree ):
    if not tree:
        return True
    
    is_balanced = abs(height(tree.left) - height(tree.right)) <= 0
    children_balanced = checkBalanced(tree.left) and checkBalanced(tree.right)
    
    return is_balanced and children_balanced


def height(node):
    
    if not node:
        return 0
    
    return max(height(node.left), height(node.right)) + 1