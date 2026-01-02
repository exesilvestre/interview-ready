# 8.  *Intersection*#
# Given two (singly) linked lists, determine if the two lists intersect.
# Return the first intersecting node. Note that the intersection is defined
# based on reference, not value.

from typing import Optional, Any

class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value
        self.next = next

def intersection(list1: Optional[Node], list2: Optional[Node]):
    seen = set()
    p1 = list1
    p2 = list2

    while p1:
        seen.add(p1)
        p1 = p1.next
    
    while p2:
        if p2 in seen:
            return p2
        p2 = p2.next
    
    return None

    