# 3. *Delete Middle Node*#
# Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node#
# ```
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f Hints: #72
# ```

from typing import Optional, Any
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def deleteMiddleNode(head: Node, position: int):
    if head is None or position <= 1:
        return head
    
    current = head
    index = 1

    while current.next and index < position - 1:
        current = current.next
        index += 1

    if current.next is None or current.next.next is None:
        return head
    
    current.next = current.next.next
    return head

    
        
