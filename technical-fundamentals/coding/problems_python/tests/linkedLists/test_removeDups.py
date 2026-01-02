from ...linkedLists.removeDups import Node, remove_dups


def linked_list_to_list(head):
    """Helper para comparar listas enlazadas"""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


def test_remove_duplicates_on_linked_list():
    node1 = Node("a")
    node2 = Node("a")
    node3 = Node("b")
    node1.next = node2
    node2.next = node3

    result = remove_dups(node1)

    assert linked_list_to_list(result) == ["a", "b"]


def test_no_duplicates_in_linked_list():
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node1.next = node2
    node2.next = node3

    result = remove_dups(node1)

    assert linked_list_to_list(result) == ["a", "b", "c"]


def test_multiple_duplicates_in_linked_list():
    node1 = Node("a")
    node2 = Node("a")
    node3 = Node("a")
    node1.next = node2
    node2.next = node3

    result = remove_dups(node1)

    assert linked_list_to_list(result) == ["a"]


def test_empty_linked_list():
    result = remove_dups(None)
    assert result is None


def test_linked_list_with_one_node():
    node1 = Node("a")

    result = remove_dups(node1)

    assert linked_list_to_list(result) == ["a"]
