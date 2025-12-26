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
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def sumLists(list1: Node, list2: Node):
    lst1 = LinkedList(list1)
    lst2 = LinkedList(list2)

    arr1 = []
    lst1.visit(lambda v: arr1.insert(0, v))

    arr2 = []
    lst2.visit(lambda v: arr2.insert(0, v))

    str1 = "".join(map(str, arr1))
    str2 = "".join(map(str, arr2))

    total = int(str1) + int(str2)

    new_list = LinkedList()
    for digit in reversed(str(total)):
        new_list.push(int(digit))

    return new_list.head
    

