

from typing import Callable, Optional


class TreeNode:
    def __init__(self, value, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right
    

class Tree:
    def bfs(self, node: Optional[TreeNode], visit: Callable[[TreeNode], None]):
        if not node:
            return None

        queue = [node]

        while queue:
            curr = queue.pop(0)
            visit(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        




    def dfs(self, node: Optional[TreeNode], visit: Callable[[TreeNode], None]):
        if not node:
            return None
        
        visit(node)
        self.dfs(node.left, visit)
        self.dfs(node.right, visit)
    