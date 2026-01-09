import pytest
from ...trees.validateBST import validateBST, TreeNode


def test_valid_bst():
    """
            Valid BST:
                 2
                / \
               1   3
    """
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert validateBST(root) is True


def test_invalid_bst_simple():
    """
            Invalid BST:
                 1
                / \
               2   3
    """
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert validateBST(root) is False


def test_invalid_bst_case_two():
    """
            Invalid BST:
                 3
                / \
               2   5
              / \
             1   4
    """
    root = TreeNode(
        3,
        TreeNode(2, TreeNode(1), TreeNode(4)),
        TreeNode(5)
    )
    assert validateBST(root) is False


def test_empty_tree():
    assert validateBST(None) is True


def test_single_node_tree():
    root = TreeNode(5)
    assert validateBST(root) is True
