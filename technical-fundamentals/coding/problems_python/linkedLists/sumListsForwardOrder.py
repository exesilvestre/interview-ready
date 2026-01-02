# 6.  Suppose the digits are stored in forward order. Repeat the above problem#
# ```
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295
# Output:9 -> 1 -> 2,That is,912.
# ```


from typing import Optional, Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


class PartialSum:
    def __init__(self):
        self.sum: Optional[Node] = None
        self.carry: int = 0

def length(node: Node) -> int:
    count = 0
    while node:
        count += 1
        node = node.next
    return count
    
def pad_lists(node: Node, padding: int) -> Node:
    for _ in range(padding):
        new_node = Node(0)
        new_node.next = node
        node = new_node
    return node

def add_lists_helper(n1: Optional[Node], n2: Optional[Node]) -> PartialSum:
    if n1 is None and n2 is None:
        return PartialSum()

    partial = add_lists_helper(n1.next, n2.next)

    total = n1.value + n2.value + partial.carry
    digit  =  total % 10
    carry = total // 10

    result_node = Node(digit)
    result_node.next = partial.sum
    partial.sum = result_node   
    partial.carry = carry
    return partial

def sumListsForwardOrder(list1: Node, list2: Node):
    len1 = length(list1)
    len2 = length(list2)

    if len1 < len2:
        list1 = pad_lists(list1, len2 - len1)
    else:
        list2 = pad_lists(list2, len1 - len2)

    partial = add_lists_helper(list1, list2)

    if partial.carry:
        result = Node(partial.carry)
        result.next = partial.sum
        return result

    return partial.sum