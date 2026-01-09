import pytest
from ...trees.checkBalanced import checkBalanced, TreeNode


def test_balanced_tree():
    """
        Balanced tree:
             1
            / \
           2   3
          / \ / \
         4  5 6  7
    """
    root = TreeNode(1,
        left=TreeNode(2,
            left=TreeNode(4),
            right=TreeNode(5)
        ),
        right=TreeNode(3,
            left=TreeNode(6),
            right=TreeNode(7)
        )
    )

    assert checkBalanced(root) is True


def test_unbalanced_tree():
    """
        Unbalanced tree:
             1
            /
           2
          /
         3
        /
       4
    """
    root = TreeNode(1,
        left=TreeNode(2,
            left=TreeNode(3,
                left=TreeNode(4)
            )
        )
    )

    assert checkBalanced(root) is False


def test_empty_tree():
    root = None
    assert checkBalanced(root) is True
