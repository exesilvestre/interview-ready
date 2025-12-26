# 4. *Partition*#
# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions#
# ```
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# ```

from typing import Optional, Any
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def partition(head: Node, x: int):
    lst = LinkedList(head)


    left = lst.filter(lambda v: v < x)
    right = lst.filter(lambda v: v > x)

    if not left:
        return right
    
    left.merge(right)
    return left.head

