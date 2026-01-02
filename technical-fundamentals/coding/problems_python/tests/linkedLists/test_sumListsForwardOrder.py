import unittest
from typing import Optional

from ...linkedLists.sumListsForwardOrder import sumListsForwardOrder, Node


class TestSumListsForwardOrder(unittest.TestCase):

    def list_to_python_list(self, head: Optional[Node]):
        """Helper para comparar listas enlazadas"""
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def test_sums_two_non_empty_lists_without_carryover(self):
        # 123 + 456 = 579
        list1 = Node(1)
        list1.next = Node(2)
        list1.next.next = Node(3)

        list2 = Node(4)
        list2.next = Node(5)
        list2.next.next = Node(6)

        result = sumListsForwardOrder(list1, list2)

        self.assertEqual(self.list_to_python_list(result), [5, 7, 9])

    def test_sums_two_non_empty_lists_with_carryover(self):
        # 999 + 1 = 1000
        list1 = Node(9)
        list1.next = Node(9)
        list1.next.next = Node(9)

        list2 = Node(1)

        result = sumListsForwardOrder(list1, list2)

        self.assertEqual(self.list_to_python_list(result), [1, 0, 0, 0])

    def test_sums_two_lists_with_different_lengths(self):
        # 1234 + 56 = 1290
        list1 = Node(1)
        list1.next = Node(2)
        list1.next.next = Node(3)
        list1.next.next.next = Node(4)

        list2 = Node(5)
        list2.next = Node(6)

        result = sumListsForwardOrder(list1, list2)

        self.assertEqual(self.list_to_python_list(result), [1, 2, 9, 0])

    def test_sums_two_empty_lists(self):
        result = sumListsForwardOrder(None, None)
        self.assertIsNone(result)

    def test_sums_one_empty_list_and_one_non_empty_list(self):
        # 123 + 0 = 123
        list1 = Node(1)
        list1.next = Node(2)
        list1.next.next = Node(3)

        result = sumListsForwardOrder(list1, None)

        self.assertEqual(self.list_to_python_list(result), [1, 2, 3])

