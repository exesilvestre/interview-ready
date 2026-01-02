#1. *Remove Dups#
#Write code to remove duplicates from an unsorted linked list. FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?#
#1 -> 2 -> 2-> 2 -> 4


from typing import Optional, Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


def remove_dups(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    p = head
    elements = set()
    elements.add(p.value)
    while p.next:
        next_node = p.next
        if next_node.value in elements:
            p.next  = p.next.next
            continue
        p = p.next
    
    return head
