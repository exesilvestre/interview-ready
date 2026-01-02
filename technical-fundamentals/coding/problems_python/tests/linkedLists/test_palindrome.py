import unittest
from typing import Optional

from ...linkedLists.palindrome import palindrome, Node


class TestIsPalindrome(unittest.TestCase):

    def test_single_node_list_is_palindrome(self):
        node = Node(1)

        result = palindrome(node)

        self.assertTrue(result)

    def test_palindrome_list_with_odd_number_of_nodes(self):
        # 1 -> 2 -> 3 -> 2 -> 1
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(2)
        node5 = Node(1)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = palindrome(node1)

        self.assertTrue(result)

    def test_non_palindrome_list(self):
        # 1 -> 2 -> 3 -> 4 -> 5
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = palindrome(node1)

        self.assertFalse(result)

    def test_palindrome_list_with_even_number_of_nodes(self):
        # 1 -> 2 -> 2 -> 1
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(2)
        node4 = Node(1)

        node1.next = node2
        node2.next = node3
        node3.next = node4

        result = palindrome(node1)

        self.assertTrue(result)