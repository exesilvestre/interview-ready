# 1. *Route Between Nodes*#
# Given a directed graph, design an algorithm to find out whether there is a route
# between two nodes.

class GraphNode:
    def __init__(self, value: int, neighbors):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []
    

def has_route_between_nodes(start: GraphNode, end: GraphNode) -> bool:
    visited = set()

    return dfs(start, end, visited)


def dfs(start, end, visited):
    if start == end:
        return True
    
    if start in visited:
        return False
    else:
        visited.add(start)
    for i in range(len(start.neighbors)):

        if start.neighbors[i]:
             if dfs(start.neighbors[i], end, visited):
                return True





