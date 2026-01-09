from ...trees.listOfDepths import listOfDepths, TreeNode, Node


# Helper para comparar linked lists
def linked_list_equal(a: Node, b: Node) -> bool:
    while a and b:
        if a.value != b.value:
            return False
        a = a.next
        b = b.next
    return a is None and b is None


# Helper para comparar listas de linked lists
def lists_of_lists_equal(result, expected):
    if len(result) != len(expected):
        return False
    for r, e in zip(result, expected):
        if not linked_list_equal(r, e):
            return False
    return True


def test_creates_linked_lists_of_nodes_at_each_depth():
    """
                    1
                   / \
                  2   3
                 / \   \
                4   5   6
               /
              7
    """
    root = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(
                4,
                left=TreeNode(7)
            ),
            right=TreeNode(5)
        ),
        right=TreeNode(
            3,
            right=TreeNode(6)
        )
    )

    expected = [
        Node(1),                                         # depth 0
        Node(2),                                         # depth 1
        Node(4),                                         # depth 2
        Node(7)                                          # depth 3
    ]

    # enlazar depth 1
    expected[1].next = Node(3)

    # enlazar depth 2
    expected[2].next = Node(5)
    expected[2].next.next = Node(6)

    result = listOfDepths(root)

    assert lists_of_lists_equal(result, expected)


def test_creates_linked_list_for_single_node():
    root = TreeNode(1)

    expected = [Node(1)]

    result = listOfDepths(root)

    assert lists_of_lists_equal(result, expected)