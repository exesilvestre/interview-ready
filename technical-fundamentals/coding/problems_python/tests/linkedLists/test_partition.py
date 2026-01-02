import unittest
from ...linkedLists.partition import partition, Node 

class TestPartition(unittest.TestCase):

    def list_values(self, head: Node) -> list:
        """Helper para convertir linked list en lista de valores"""
        values = []
        current = head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def test_partitions_list_correctly(self):
        # 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
        node1 = Node(3)
        node2 = Node(5)
        node3 = Node(8)
        node4 = Node(5)
        node5 = Node(10)
        node6 = Node(2)
        node7 = Node(1)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7

        result = partition(node1, 5)

        # valores esperados: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
        expected = [3, 2, 1, 5, 8, 5, 10]
        self.assertEqual(self.list_values(result), expected)

    def test_single_node(self):
        node1 = Node(5)
        result = partition(node1, 5)
        self.assertEqual(self.list_values(result), [5])

    def test_all_nodes_less_than_x(self):
        # 3 -> 2 -> 1 -> 4 -> 5
        node1 = Node(3)
        node2 = Node(2)
        node3 = Node(1)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = partition(node1, 6)
        expected = [3, 2, 1, 4, 5]
        self.assertEqual(self.list_values(result), expected)

    def test_all_nodes_greater_or_equal_x(self):
        # 3 -> 2 -> 1 -> 4 -> 5
        node1 = Node(3)
        node2 = Node(2)
        node3 = Node(1)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        result = partition(node1, 0)
        expected = [3, 2, 1, 4, 5]
        self.assertEqual(self.list_values(result), expected)


if __name__ == "__main__":
    unittest.main()
