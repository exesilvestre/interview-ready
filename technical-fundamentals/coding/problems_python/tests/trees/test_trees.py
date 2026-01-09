import unittest
from ...trees.trees import TreeNode, Tree

class TestTrees(unittest.TestCase):

    def test_dfs_navigates_the_tree_in_order(self):
        root = TreeNode(
            value=1,
            left=TreeNode(
                value=2,
                left=TreeNode(value=3),
                right=TreeNode(value=4)
            ),
            right=TreeNode(
                value=5,
                left=TreeNode(
                    value=6,
                    left=TreeNode(value=7)
                ),
                right=TreeNode(value=8)
            )
        )

        tree = Tree()
        order = []
        tree.dfs(root, lambda node: order.append(node))
        self.assertEqual([n.value for n in order], [1, 2, 3, 4, 5, 6, 7, 8])


    def test_bfs_navigates_the_tree_in_order(self):
        root = TreeNode(
            value=1,
            left=TreeNode(
                value=2,
                left=TreeNode(value=4),
                right=TreeNode(value=5)
            ),
            right=TreeNode(
                value=3,
                left=TreeNode(
                    value=6,
                    left=TreeNode(value=8)
                ),
                right=TreeNode(value=7)
            )
        )

        tree = Tree()
        order = []
        tree.bfs(root, lambda node: order.append(node))
        self.assertEqual([n.value for n in order], [1, 2, 3, 4, 5, 6, 7, 8])


