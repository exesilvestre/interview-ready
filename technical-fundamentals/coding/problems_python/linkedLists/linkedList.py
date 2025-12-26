from typing import Any, Optional, Callable


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0

    def push(self, value: Any) -> None:
        new_node = Node(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def visit(self, fn: Callable[[Any], None]) -> None:
        current = self.head
        while current:
            fn(current.value)
            current = current.next

    def filter(self, predicate: Callable[[Any], bool]) -> "LinkedList":
        result = LinkedList()
        current = self.head

        while current:
            if predicate(current.value):
                result.push(current.value)
            current = current.next

        return result

    def remove(self, value: Any) -> bool:
        current = self.head
        prev = None

        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next

                if current == self.tail:
                    self.tail = prev

                self.length -= 1
                return True

            prev = current
            current = current.next

        return False

    def merge(self, other: "LinkedList") -> None:
        if not other.head:
            return

        if not self.head:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail

        self.length += other.length

    def print(self) -> None:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values))