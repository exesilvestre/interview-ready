# 3. *List of Depths*#
# Given a binary tree, design an algorithm which creates a linked list
# of all the nodes at each depth (e.g., if you have a tree with depth D,
# you'll have D linked lists).

from typing import Any, Optional


class TreeNode:
    def __init__(self, value, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None
        

def listOfDepths(root):
    if not root:
        return None
    
    result = []
    queue = [root]

    while queue:
        head = None
        tail = None
        for i in range(len(queue)):
            curr = queue.pop(0)
            new_node = Node(curr.value)
            if head is None:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        result.append(head)
    
    return result


