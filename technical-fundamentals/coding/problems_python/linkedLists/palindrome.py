# 7. *Palindrome


# Implement a function to check if a linked list is a palindrome.


from typing import Optional, Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def palindrome(head: Node):
    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    
    return True
    