import unittest
from ...linkedLists.intersection import Node, intersection

class TestIntersection(unittest.TestCase):
    
    def test_no_intersection(self):
        # Lista 1: 1 -> 2 -> 3 -> 4
        # Lista 2: 5 -> 6 -> 7 -> 8
        list1 = Node(1, Node(2, Node(3, Node(4))))
        list2 = Node(5, Node(6, Node(7, Node(8))))
        result = intersection(list1, list2)
        self.assertIsNone(result)

    def test_intersection_middle(self):
        # Parte común: 7 -> 8 -> 9
        common = Node(7, Node(8, Node(9)))
        # Lista 1: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
        list1 = Node(1, Node(2, Node(3, Node(4, common))))
        # Lista 2: 5 -> 6 -> 7 -> 8 -> 9
        list2 = Node(5, Node(6, common))
        result = intersection(list1, list2)
        self.assertIs(result, common)  # verificamos la misma referencia

    def test_intersection_head(self):
        # Parte común: 1 -> 2 -> 3
        common = Node(1, Node(2, Node(3)))
        result = intersection(common, common)
        self.assertIs(result, common)

    def test_intersection_end(self):
        # Lista 1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        list1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
        # Lista 2: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        list2 = Node(0, list1)
        result = intersection(list1, list2)
        self.assertIs(result, list1)


if __name__ == "__main__":
    unittest.main()
