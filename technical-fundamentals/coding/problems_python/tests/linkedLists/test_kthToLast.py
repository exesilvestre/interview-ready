import unittest
from typing import Any, Optional
from ...linkedLists.kthToLast import kthToLast, Node  # reemplaza 'your_module' por tu archivo real

class TestKthToLast(unittest.TestCase):

    def test_k_less_than_1(self):
        node1 = Node(1)
        result = kthToLast(node1, 0)
        self.assertIsNone(result)  # equivale a "undefined" en JS

    def test_k_greater_than_length(self):
        node1 = Node(1)
        result = kthToLast(node1, 2)
        self.assertIsNone(result)

    def test_k_valid(self):
        # Crear lista enlazada: 1 -> 2 -> 3 -> 4 -> 5
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = kthToLast(node1, 2)
        self.assertIs(result, node4)  # verificamos la misma referencia

    def test_k_equals_length(self):
        # Crear lista enlazada: 1 -> 2 -> 3 -> 4 -> 5
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = kthToLast(node1, 5)
        self.assertIs(result, node1)  # devuelve la cabeza de la lista


if __name__ == "__main__":
    unittest.main()
