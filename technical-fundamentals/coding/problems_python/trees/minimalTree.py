from typing import Callable, List, Optional

# 2. *Minimal Tree*#
# Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.
#
# A binary search tree is a search where for each node,
# lesser elements are on the left node, and greater elements on the right node.
#
# Input: [1,2,3,4,5,6,7,8]
# Output:
#      5
#   2  |  7
# 1   3|6   8
#
#


class TreeNode:
    def __init__(self, value, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

def minimalTree(sortedArray: List):
    if len(sortedArray) == 0:
        return None
    
    pivot_index = len(sortedArray) // 2
    pivot = sortedArray[pivot_index]

    left = minimalTree(sortedArray[:pivot_index])
    right = minimalTree(sortedArray[pivot_index + 1:])
    
    return TreeNode(pivot, left, right)

"""
[1,2,3,4,5,6,7,8]
1 pivot = 5
2 pivot = 3
3 pivot = 2
4 pivot = 1
5 return None




"""