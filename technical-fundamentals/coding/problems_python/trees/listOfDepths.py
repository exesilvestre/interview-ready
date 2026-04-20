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
        return []
    
    queue = [root]
    results = []

    while queue:
        head = None
        tail = None
        for i in range(len(queue)):
            curr = queue.pop(0)
            node = Node(curr.value)
            if not head:
                tail = head = node
            else:
                tail.next = node
                tail = node
            
        
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        results.append(head)
    
    return results

