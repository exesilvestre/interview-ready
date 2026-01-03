# 5. *Sum Lists*: You have two numbers represented by a linked list,
# where each node contains a single digit. The digits are stored in reverse order,
# such that the Vs digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list#
# ```
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# ```

from typing import Optional, Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def sumLists(list1: Node, list2: Node):
    carry = 0
    result_head = result_tail = None

    p1 = list1
    p2 = list2

    while p1 or p2 or carry:
        val1 = p1.value if p1 else 0
        val2 = p2.value if p2 else 0

        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10

        new_node = Node(digit)

        if not result_head:
            result_head = result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = new_node
        
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next
    
    return result_head


