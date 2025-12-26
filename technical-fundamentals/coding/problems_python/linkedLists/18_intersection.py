# 8.  *Intersection*#
# Given two (singly) linked lists, determine if the two lists intersect.
# Return the first intersecting node. Note that the intersection is defined
# based on reference, not value.

from typing import Optional, Any
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def intersection(list1: Node, list2: Node):
    seen = set()
    current = list1
    while current:
        seen.add(current)
        current = current.next

    current = list2
    while current:
        if current in seen:
            return current
        current = current.next

    return None

    