import unittest
from typing import Optional

from ...linkedLists.loopDetection import loopDetection, Node


class TestLoopDetection(unittest.TestCase):

    def test_returns_none_if_list_has_only_one_node(self):
        node = Node(1)

        result = loopDetection(node)

        self.assertIsNone(result)

    def test_returns_none_if_list_does_not_have_loop(self):
        # List: 1 -> 2 -> 3 -> 4 -> 5
        list_head = Node(1)
        list_head.next = Node(2)
        list_head.next.next = Node(3)
        list_head.next.next.next = Node(4)
        list_head.next.next.next.next = Node(5)

        result = loopDetection(list_head)

        self.assertIsNone(result)

    def test_returns_node_at_beginning_of_loop(self):
        # Loop: 31 -> 32 -> 31
        loop_node = Node(31)
        loop_node.next = Node(32)
        loop_node.next.next = loop_node

        # List:
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 31 -> 32 -> 31
        head = Node(1)
        current = head
        for value in [2, 3, 4, 5, 6, 7, 8, 9]:
            current.next = Node(value)
            current = current.next

        current.next = loop_node

        result = loopDetection(head)

        self.assertIs(result, loop_node)

    def test_returns_node_at_beginning_of_longer_loop(self):
        # Loop: 11 -> 12 -> 13 -> 11
        loop_node = Node(11)
        loop_node.next = Node(12)
        loop_node.next.next = Node(13)
        loop_node.next.next.next = loop_node

        # List:
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> ...
        head = Node(1)
        current = head
        for value in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            current.next = Node(value)
            current = current.next

        current.next = loop_node

        result = loopDetection(head)

        self.assertIs(result, loop_node)