# 6.  Suppose the digits are stored in forward order. Repeat the above problem#
# ```
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295
# Output:9 -> 1 -> 2,Thatis,912.
# ```


from typing import Optional, Any
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def sumListsForwardOrder(list1: Node, list2: Node):
    lst1 = LinkedList(list1)
    lst2 = LinkedList(list2)
    if not lst1 or not lst2:
        return None

    arr1 = []
    lst1.visit(lambda v: arr1.append(str(v)))

    arr2 = []
    lst2.visit(lambda v: arr2.append(str(v)))

    n1 = int("".join(arr1))
    n2 = int("".join(arr2))

    total = n1 + n2

    new_list =LinkedList()
    for i in str(total):
        new_list.push(int(i))


    return new_list.head