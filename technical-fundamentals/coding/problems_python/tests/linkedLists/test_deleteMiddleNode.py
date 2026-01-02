import pytest
from typing import Optional, Any
from ...linkedLists.deleteMiddleNode import Node, deleteMiddleNode

def test_deletes_middle_node_at_position_1():
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)

    result = deleteMiddleNode(head, 1)

    assert result.value == 0
    assert result.next.value == 2
    assert result.next.next.value == 3
    assert result.next.next.next is None


def test_no_deletion_if_position_out_of_range():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = deleteMiddleNode(head, 4)

    expected_value = 1
    current = result
    while current:
        assert current.value == expected_value
        expected_value += 1
        current = current.next


def test_no_deletion_if_position_less_than_1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = deleteMiddleNode(head, 0)

    expected_value = 1
    current = result
    while current:
        assert current.value == expected_value
        expected_value += 1
        current = current.next


def test_no_deletion_if_list_has_one_node():
    head = Node(1)

    result = deleteMiddleNode(head, 2)

    assert result.value == 1
    assert result.next is None


def test_no_deletion_if_list_has_two_nodes():
    head = Node(1)
    head.next = Node(2)

    result = deleteMiddleNode(head, 2)

    assert result.value == 1
    assert result.next.value == 2
    assert result.next.next is None