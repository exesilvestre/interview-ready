import unittest
from ...trees.hasRouteBetweenNodes import has_route_between_nodes, GraphNode  


class TestHasRouteBetweenNodes(unittest.TestCase):

    def test_has_route_between_connected_nodes(self):
        """
                Graph:
                1 -> 2 -> 3 -> 4
                |         |
                5         6
        """

        node1 = GraphNode(1, [])
        node2 = GraphNode(2, [])
        node3 = GraphNode(3, [])
        node4 = GraphNode(4, [])
        node5 = GraphNode(5, [])
        node6 = GraphNode(6, [])

        node1.neighbors = [node2, node5]
        node2.neighbors = [node3]
        node3.neighbors = [node4, node6]
        node6.neighbors = [node3]  # cycle/back edge

        self.assertTrue(has_route_between_nodes(node1, node4))
        self.assertFalse(has_route_between_nodes(node4, node1))  # No reverse route
        self.assertFalse(has_route_between_nodes(node2, node5))  # No direct route
        self.assertTrue(has_route_between_nodes(node1, node6))  # Route via node3

    def test_no_route_between_disconnected_nodes(self):
        """
                Graph:
                1   2   3
                |___|___|
        """

        node1 = GraphNode(1, [])
        node2 = GraphNode(2, [])
        node3 = GraphNode(3, [])

        self.assertFalse(has_route_between_nodes(node1, node2))
        self.assertFalse(has_route_between_nodes(node2, node3))
        self.assertFalse(has_route_between_nodes(node1, node3))

    def test_no_route_between_non_existing_nodes(self):
        node1 = GraphNode(1, [])
        node2 = GraphNode(2, [])

        self.assertFalse(has_route_between_nodes(node1, node2))



