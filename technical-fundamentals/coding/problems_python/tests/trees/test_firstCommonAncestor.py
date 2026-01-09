import unittest
from ...trees.firstCommonAncestor import firstCommonAncestor, TreeNode


def create_node(value, left=None, right=None):
    return TreeNode(value, left, right)


class TestFirstCommonAncestor(unittest.TestCase):

    def test_common_ancestor_valid_input(self):
        """
                       1
                      / \
                     2   3
                    / \ / \
                   4  5 6  7
        """

        root = create_node(
            1,
            create_node(2, create_node(4), create_node(5)),
            create_node(3, create_node(6), create_node(7)),
        )

        # Common ancestor of 2 and 3 is 1
        self.assertIs(firstCommonAncestor(root, root.left, root.right), root)

        # Common ancestor of 4 and 5 is 2
        self.assertIs(firstCommonAncestor(root, root.left.left, root.left.right), root.left)

        # Common ancestor of 4 and 7 is 1
        self.assertIs(firstCommonAncestor(root, root.left.left, root.right.right), root)

