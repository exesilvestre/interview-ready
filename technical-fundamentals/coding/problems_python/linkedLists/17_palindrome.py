# 7. *Palindrome


# Implement a function to check if a linked list is a palindrome.


from typing import Optional, Any
from linkedList import LinkedList

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None

def palindrome(head: Node):
    lst = LinkedList(head)

    chars = []
    lst.visit(lambda v: chars.append(v))

    word = "".join(chars)

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False

    return True