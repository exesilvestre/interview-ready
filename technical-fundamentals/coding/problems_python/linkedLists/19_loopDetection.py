# 9. *Loop Detection*#
# Given a circular linked list, implement an algorithm that returns the node
# at the beginning of the loop#
# ```
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
# ``#
# ```
# EXAMPLE
# Input: A->8->C->D->E-> C[thesameCasearlier] Output: C
# Hints: #50, #69, #83, #90
# ```


from typing import Optional, Any
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def loopDetection(head: Node):
    seen = set()
    current = head

    while current:
        if current in seen:
            return current
        seen.add(current)
        current = current.next

    