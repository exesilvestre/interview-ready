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

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def partition(head: Node, x: int):
    if head is None:
        return None
    
    left_tail = left_head = None
    right_tail = right_head = None

    current = head
    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            if left_head is None:
                left_head = left_tail = current
            else:
                left_tail.next = current
                left_tail = current
                
        else:
            if right_head is None:
                right_head = right_tail = current
            else:
                right_tail.next = current
                right_tail = current
                
            
        current = next_node
    
    if left_tail:
        left_tail.next = right_head
        return left_head
    else:
        return right_head