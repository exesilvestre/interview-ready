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
    seen = set()
    seen.add(head.value)

    current = head
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next 
        else:
            seen.add(current.next.value)
            current = current.next

    return head
