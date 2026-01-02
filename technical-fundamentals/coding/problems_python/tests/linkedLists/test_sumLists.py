import unittest
from typing import Optional

from ...linkedLists.sumLists import sumLists, Node   

def linked_list_to_list(head: Optional[Node]) -> list:
    """Convierte una linked list a una lista de Python"""
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values


class TestSumLists(unittest.TestCase):

    def test_sums_two_non_empty_lists_without_carryover(self):
        # 321 + 654 = 975

        # list1 = 1 -> 2 -> 3
        list1 = Node(1)
        list1.next = Node(2)
        list1.next.next = Node(3)

        # list2 = 4 -> 5 -> 6
        list2 = Node(4)
        list2.next = Node(5)
        list2.next.next = Node(6)

        result = sumLists(list1, list2)

        expected = [5, 7, 9]
        self.assertEqual(linked_list_to_list(result), expected)

    def test_sums_two_non_empty_lists_with_carryover(self):
        # 999 + 1 = 1000

        # list1 = 9 -> 9 -> 9
        list1 = Node(9)
        list1.next = Node(9)
        list1.next.next = Node(9)

        # list2 = 1
        list2 = Node(1)

        result = sumLists(list1, list2)

        expected = [0, 0, 0, 1]
        self.assertEqual(linked_list_to_list(result), expected)

    def test_sums_two_lists_with_different_lengths(self):
        # 4321 + 65 = 4386

        # list1 = 1 -> 2 -> 3 -> 4
        list1 = Node(1)
        list1.next = Node(2)
        list1.next.next = Node(3)
        list1.next.next.next = Node(4)

        # list2 = 5 -> 6
        list2 = Node(5)
        list2.next = Node(6)

        result = sumLists(list1, list2)

        expected = [6, 8, 3, 4]
        self.assertEqual(linked_list_to_list(result), expected)

