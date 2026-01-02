# 2.  *Return Kth to Last*#
# Implement an algorithm to find the kth to last element of a singly linked list.


from typing import Optional, Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


def kthToLast(head: Node, k: int):
    if not head or k <= 0:
        return None
    
    original = head
    advanced = head

    for i in range(k):
        if not advanced:
            return None
        advanced = advanced.next
    
    while advanced:
        original = original.next
        advanced = advanced.next
    
    return original
