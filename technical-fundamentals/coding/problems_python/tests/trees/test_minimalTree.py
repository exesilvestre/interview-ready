import pytest
from ...trees.minimalTree import minimalTree, TreeNode


# --- helper interno para comparar árboles ---
def trees_equal(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (
        a.value == b.value and
        trees_equal(a.left, b.left) and
        trees_equal(a.right, b.right)
    )


def test_creates_minimal_height_bst_from_sorted_array():
    sorted_array = [1, 2, 3]
    expected_tree = TreeNode(
        2,
        left=TreeNode(1),
        right=TreeNode(3)
    )
    assert trees_equal(minimalTree(sorted_array), expected_tree)


def test_creates_minimal_height_bst_from_sorted_array_5_length():
    sorted_array = [1, 2, 3, 4, 5]
    expected_tree = TreeNode(
        3,
        left=TreeNode(
            2,
            left=TreeNode(1)
        ),
        right=TreeNode(
            5,
            left=TreeNode(4)
        )
    )
    assert trees_equal(minimalTree(sorted_array), expected_tree)


def test_creates_minimal_height_bst_from_sorted_array_7_length():
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    expected_tree = TreeNode(
        4,
        left=TreeNode(
            2,
            left=TreeNode(1),
            right=TreeNode(3)
        ),
        right=TreeNode(
            6,
            left=TreeNode(5),
            right=TreeNode(7)
        )
    )
    assert trees_equal(minimalTree(sorted_array), expected_tree)


def test_returns_none_for_empty_array():
    sorted_array = []
    assert minimalTree(sorted_array) is None